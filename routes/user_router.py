from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi import Request
from http import HTTPStatus
import uuid
from utils.exception_handler import *
from utils.cjwt import JWTBearer, get_password_hash, is_valid_password
from utils.file_uploader import *
from schemas.User import (LoginRequest, UserResult, UserUpdateProfile, UserChangePassword)
from schemas.Resp import GenResponse
from repos.user import UserRepo
import traceback
from schemas.Resp import GenResponse
# from fastapi.encoders import jsonable_encoder


router = APIRouter(
            prefix='/auth2',
            tags=['Auth2'],
            responses={422: {"message": "Request failed"}}
        )

auth_bearer = JWTBearer()

# #create an account
@router.post("/login")
def admin_login(req_data:LoginRequest, request:Request):
    try:
        db_user = UserRepo.fetch_by_email(req_data.email)
        role = {}
        print("USER", str(db_user))
        # print("USER", str(db_user.serialize()))
        if db_user and db_user["_relationships"] and db_user["_relationships"]["role"]:
            tmp = db_user["_relationships"]["role"]
            role = {
                "id": tmp.id,
                "name": tmp.name,
                "description": tmp.description,
            }
        # print("ROLE", role)

        err_resp = GenResponse(
                    message="Invalid login credentials provided",
                    status_code=HTTPStatus.UNAUTHORIZED, data=None,
                )
        if not db_user:
            return err_resp #//return response

        tmp_user = db_user.as_dict()
        del db_user
        pwd_verified = is_valid_password(req_data.password, tmp_user["password"])
        if not pwd_verified:         
            return err_resp #//return response

        del tmp_user["password"]
        jwt_token= JWTBearer.sign_jwt(tmp_user)
        tmp_user["role_relationship"] = role
        return {
            'message': 'Login Successful', 
            'access_token':jwt_token.get("token"), 
            'expires_at':jwt_token.get('expires_at'), 
            'data':tmp_user,
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/user/profile")
def get_current_user_profile(request:Request, token:str=Depends(auth_bearer)):
    # dec_token = JWTBearer().decode_jwt(token)
    dec_token = auth_bearer.decode_jwt(token)
    user_id = dec_token.get("sub")

    current_user = UserRepo.fetch_by_id_min(user_id).serialize()
    # print("CURR USER", current_user)
            
    return GenResponse(
                message="Current user details retrieved successfully!",
                status_code=HTTPStatus.OK, 
                data=current_user,
            )


@router.put("/update/profile")
async def update_user_profile(profile:UserUpdateProfile, request:Request, token:str=Depends(auth_bearer)):
    msg = "Invalid login credentials provided",
    code = HTTPStatus.UNAUTHORIZED
    
    # dec_token = decodeJWT(token)
    dec_token = auth_bearer.decode_jwt(token)
    user_id = dec_token.get("sub")

    update_res = await UserRepo.update_profile(user_id, profile)
    print("PROFILE RES", update_res)
            
    return GenResponse(
                message="User profile updated successfully!",
                status_code=HTTPStatus.OK, 
                data=update_res,
            )


@router.put("/update/change-password")
async def update_user_password(req: UserChangePassword, request:Request, token:str=Depends(auth_bearer)):
    msg = "Invalid credentials provided",
    code = HTTPStatus.UNAUTHORIZED

    # check if new password == old pasword
    if(req.current_password == req.password):
        return GenResponse(
                message="Sorry!, current password and new password must not be the equal",
                status_code=code, 
                data=None,
            )

    # dec_token = decodeJWT(token)
    dec_token = auth_bearer.decode_jwt(token)
    user_id = dec_token.get("sub")

    current_user = UserRepo.fetch_by_id(user_id)
    print("CURR USER", current_user, )
    if is_valid_password(req.current_password, current_user.get("password")):
        print("CHK 1", "Password is valid")

        pwd_hashed = get_password_hash(req.password)
        upd_res:UserResult = await UserRepo.change_password(user_id, pwd_hashed)
        if upd_res.get("data"):
            msg = "User password changed successfully!"
            code = HTTPStatus.OK

        print("RES", upd_res)
    else:
        msg = "Wrong password provided"
        code = HTTPStatus.FORBIDDEN
            
    return GenResponse(
                message=msg,
                status_code=code, 
                data=current_user,
            )
