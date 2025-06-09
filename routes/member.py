from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi import Request
from http import HTTPStatus
import uuid
from utils.exception_handler import *
from utils.cjwt import JWTMemberBearer, get_password_hash, is_valid_password
# from fastapi import UploadFile, File
from utils.file_uploader import *
from schemas.musiga.Member import MemberSetPassword, MemberLoginRequest
from schemas.Resp import GenResponse
from repos.auth import AdminRepo
from repos.member import MemberRepo
import traceback, logging
from schemas.Resp import GenResponse
# from fastapi.encoders import jsonable_encoder

logger = logging.getLogger(__name__)

router = APIRouter(
            prefix='/member',
            tags=['Member'],
            responses={422: {"message": "Request failed"}}
        )

auth_bearer = JWTMemberBearer()


#create an account
@router.post("/hash")
async def register(pwd:str, response:Response): 
    try:
        pwd_hash = get_password_hash(pwd)
        pwd = pwd_hash
        resp = {
            "id": str(uuid.uuid4()),
            "pass": pwd,
        }

        return GenResponse(
            data=resp,
            status_code=HTTPStatus.OK,
            message="Resource retrieved sucessfully!"
        )

    except Exception as e:     
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post("/set-password")
async def set_member_password(req:MemberSetPassword, request:Request):
    msg = "Invalid credentials provided",
    code = HTTPStatus.UNAUTHORIZED
    res = None

    is_phone_no = False
    if req.login_id.isnumeric():
        is_phone_no = True
        
    print("Login ID", req.login_id, f"Is numeric: {is_phone_no}")    
    member = MemberRepo.fetch_by_email_or_phone_no_combo(req.login_id, is_phone_no)
    print("CURR USER", member, )
    if member:
        if req.password == req.password_confirmation:
            pwd_hash = get_password_hash(req.password)
            print("Member Found", f"Password: {pwd_hash}")
            upd_res = await MemberRepo.set_member_password(member.get("id"), pwd_hash)
            print(f"Member [{member.get('id')}] updated", upd_res)
            if upd_res.get("data"):
                msg = "User password changed successfully!"
                code = HTTPStatus.OK

        else:
            msg = "Password and Password confirmation do not match"

    return GenResponse(
                message=msg,
                status_code=code, 
                data=member,
            )


# #create an account
@router.post("/login")
def member_login(req_data:MemberLoginRequest, request:Request):
    try:
        is_phone_no = False
        if req_data.login_id.isnumeric():
            is_phone_no = True

        db_user = MemberRepo.fetch_by_id_for_login(req_data.login_id, is_phone_no)
        print("USER", str(db_user))
        err_resp = GenResponse(
                    message="Invalid login credentials provided",
                    status_code=HTTPStatus.UNAUTHORIZED, data=None,
                )
        if not db_user:
            return err_resp #//return response

        tmp_user = db_user
        del db_user
        pwd_verified = is_valid_password(req_data.password, tmp_user["password"])
        if not pwd_verified:         
            return err_resp #//return response

        del tmp_user["password"]
        jwt_token= JWTMemberBearer.sign_jwt(tmp_user)

        return {
            'message': 'Login Successful', 
            'access_token':jwt_token.get("token"), 
            'expires_at':jwt_token.get('expires_at'), 
            'data':tmp_user,
        }
       
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get(" /profile")
def get_current_user_profile(request:Request, token:str=Depends(auth_bearer)):
    dec_token = JWTMemberBearer().decode_jwt(token)
    # print("TOKEN", token, "DECODED", dec_token)
    # user_id = dec_token.get("sub")

    current_user = MemberRepo.fetch_single_by_id(dec_token.get("sub"))
    # print("CURR USER", current_user)
            
    return GenResponse(
                message="Current user details retrieved successfully!",
                status_code=HTTPStatus.OK, 
                data=current_user,
            )


# @router.put("/profile")
# async def update_user_profile(profile:AdminUpdateProfile, request:Request, token:str=Depends(auth_bearer)):
#     msg = "Invalid login credentials provided",
#     code = HTTPStatus.UNAUTHORIZED
    
#     dec_token = decodeJWT(token)
#     user_id = dec_token.get("sub")

#     update_res = await AdminRepo.update_profile(user_id, profile)
#     print("PROFILE RES", update_res)
            
#     return GenResponse(
#                 message="User profile updated successfully!",
#                 status_code=HTTPStatus.OK, 
#                 data=update_res,
#             )


from routes.admin.services import getNextMemberId
from schemas.musiga.Member import MemberCreate
from repos.musiga.mem_educ_n_contact import (
    MemberEducRepo, RelatedContactRepo
)

@router.post("/register")
async def add_new_member(
    request:Request,
    req: MemberCreate,
    # token: str = Depends(adm_bearer),
):
    
    # add image to s3 bucket if image_url is not empty
    req.image_url = None
    # req.passport_image = None
    if req.image_url and req.image_url != "":
        logger.warning("Member image provided but not yet uploaded")
        pass
    
    member_id = getNextMemberId()
    req.member_id = member_id

    if req.password:
        pwd_hash = get_password_hash(req.password)
        req.password = pwd_hash
        print("Member Found", f"Password: {pwd_hash}")
        del pwd_hash
        pass
    req.active_status = 'pending'
    mem_res = await MemberRepo.create(req)
    res_tmp = mem_res["data"] if mem_res["data"] else None
    res = {"errors": {}, "data": {}}

    msg = "Member registration could not be completed."
    code = HTTPStatus.BAD_REQUEST
    if res_tmp:
        entry_id = res_tmp.get('id')
        res["data"]["member"] = res_tmp
        
        # 1. add educational detail
        if req.education and len(req.education) > 0:
            # print("EDU", req.education)
            edu_res = await MemberEducRepo.create_bulk(req.education, entry_id)
            if edu_res['data'] and len(edu_res['data']) > 0:
                res['data']["education"] = edu_res['data']

            if edu_res['errors'] and len(edu_res['errors']) > 0:
                res['errors']["education"] = edu_res['errors']
            logger.warning("EDU :: RES")
            logger.warning(edu_res)

        # 2. add related contact detail
        if req.related_contact and len(req.related_contact) > 0:
            # print("RELC", req.related_contact)
            relc_res = await RelatedContactRepo.create_bulk(req.related_contact, entry_id)
            if relc_res['data'] and len(relc_res['data']) > 0:
                res['data']["rel_contact"] = relc_res['data']

            if relc_res['errors'] and len(relc_res['errors']) > 0:
                res['errors']["rel_contact"] = relc_res['errors']
            logger.warning("RELC :: RES")
            logger.warning(relc_res)
            pass

    if mem_res["errors"]:
        res["errors"]["member"] = mem_res["errors"]

    if not res["errors"]:
        msg = "Member registration completed successfully!"
        code = HTTPStatus.CREATED
    
    return {
        "message": msg,
        "status_code": code,
        "data": res
    }

