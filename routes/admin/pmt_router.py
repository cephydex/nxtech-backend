from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi import Request
from http import HTTPStatus
import uuid, logging
from utils.exception_handler import *
from utils.cjwt import JWTBearer, get_password_hash, is_valid_password
# from fastapi import UploadFile, File
from utils.file_uploader import *
# from schemas.Auth import LoginRequest, AdminChangePassword, AdminUpdateProfile
from schemas.Resp import GenResponse
# from repos.auth import AdminRepo
import traceback
import requests
# from fastapi.encoders import jsonable_encoder


router = APIRouter(
            prefix='/pmt',
            tags=['Pmt'],
            responses={422: {"message": "Request failed"}}
        )

auth_bearer = JWTBearer()
logger = logging.getLogger(__name__)


#create an account
@router.get("/pay_init")
async def register(pwd:str, response:Response): 
    try:
        pwd_hash = get_password_hash(pwd)
        pwd = pwd_hash
        resp = {
            "id": str(uuid.uuid4()),
            "pass": pwd,
        }
        
        # var username = _configuration.GetValue<string>("Payment:Username");
        #     var password = _configuration.GetValue<string>("Payment:Password");
        #     var authString = $"{username}:{password}";

        return GenResponse(
            data=resp,
            status_code=HTTPStatus.OK,
            message="Resources retrieved successfully!"
        )

    except Exception as e:     
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

from utils.lib import Hubtel
from schemas.Payment import PaymentHubtelCallback, PaymentRequestSchema
#create an account
@router.post("/initiate")
async def init_payment(request: PaymentRequestSchema, response:Response): 
    try:
        hubtel = Hubtel()
        phone_no = request.phone_no
        phone_no = phone_no if not phone_no.startswith('0') else '233'+ phone_no[1:]
        
        # initiate payment provider
        payment_res = hubtel.initiate_payment(
            amount=2.0,
            description='MUSIGA dues payment',
            client_reference=str(uuid.uuid4()),
            return_url='https://musigap-be-staging.gmxofficial.com/api/v1/payments/callback',
        )
        
        print('payment result', payment_res)
        
        
        resp = {
            "phone_no": request.phone_no,
            'data': payment_res,
        }
        
        # var username = _configuration.GetValue<string>("Payment:Username");
        #     var password = _configuration.GetValue<string>("Payment:Password");
        #     var authString = $"{username}:{password}";

        return GenResponse(
            data=resp,
            status_code=HTTPStatus.OK,
            message="Resources retrieved successfully!"
        )

    except Exception as e:     
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post("/prompt")
async def init_payment(request: PaymentRequestSchema, response:Response): 
    try:
        hubtel = Hubtel()
        phone_no = request.phone_no
        phone_no = phone_no if not phone_no.startswith('0') else '233'+ phone_no[1:]
        description =  "MUSIGA dues payment"
        
        payment_res = hubtel.initiate_prompt(
            phone_no=phone_no,
            amount=2.0,
            client_reference=str(uuid.uuid4()),
            description=description,
            channel= 'mtn-gh',
        )
        
        print('payment result', payment_res)
        resp = {
            "phone_no": request.phone_no,
            'data': payment_res,
        }
        
        # "Username": "zB59YEy",
        # "Password": "2b993949ec65467c9eccf91ae9fa8ffd",
        # "Base64Auth": "ekI1OVlFeToyYjk5Mzk0OWVjNjU0NjdjOWVjY2Y5MWFlOWZhOGZmZAo=",
        # "Receive": "https://rmp.hubtel.com/merchantaccount/merchants/2016799/receive/mobilemoney",
    
        # var username = _configuration.GetValue<string>("Payment:Username");
        #     var password = _configuration.GetValue<string>("Payment:Password");
        #     var authString = $"{username}:{password}";

        return GenResponse(
            data=resp,
            status_code=HTTPStatus.OK,
            message="Resources retrieved successfully!"
        )

    except Exception as e:     
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")



# @router.post("/initiate_callback", response_model=GenResponse)
@router.post("/initiate_callback", response_model=GenResponse)
def initiate_callback(request: PaymentHubtelCallback, response: Response):
    try:
        # hasura = Hasura()
        # utils = Utils()

        updated_by = {
            "id": "00000000-0000-0000-0000-000000000002",
            "username": "hubtel",
            "name": "Hubtel Callback",
        }

        # only success when you're 100% sure, because payment platforms
        status = "failed"
        if request.Status == "Success":
            status = "success"
            
    except Exception as err:
        logger.error(f"PUT :: payment initiate callback")
        logger.exception(err)
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        return GenResponse(message="internal server error")


# @router.get("/user/profile")
# def get_current_user_profile(request:Request, token:str=Depends(auth_bearer)):
#     # dec_token = JWTBearer().decode_jwt(token)
#     dec_token = auth_bearer.decode_jwt(token)
#     user_id = dec_token.get("sub")

#     current_user = AdminRepo.fetch_by_id_min(user_id).serialize()
#     # print("CURR USER", current_user)
            
#     return GenResponse(
#                 message="Current user details retrieved successfully!",
#                 status_code=HTTPStatus.OK, 
#                 data=current_user,
#             )

