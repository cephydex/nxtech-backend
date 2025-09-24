from .model import PolicyCreate
from .service import PolicyRepo
from fastapi import APIRouter, Request, Depends
import logging
from utils.cjwt import JWTBearer
from http import HTTPStatus
from schemas.Resp import GenResponse


logger = logging.getLogger(__name__)
router = APIRouter(
            prefix='/func',
            tags=['Func'],
            responses={422: {"message": "Request failed"}}
        )

auth_bearer = JWTBearer()


@router.post("/policies")
async def create_policy(req_d:PolicyCreate, request:Request, token:str=Depends(auth_bearer)):
    # userId = auth_bearer.get_user_id(token)
    req_d.created_by = str(auth_bearer.get_user_id(token))

    result = await PolicyRepo.create(req_d)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    
    msg = "Policy created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Policy could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg,
                status_code=code, 
                data=result,
            )


@router.get("/policies/{policy_id}")
def get_policy_by_id(policy_id:str, token:str=Depends(auth_bearer)):
    result = PolicyRepo.fetch_by_id(policy_id)
    
    return GenResponse(
                message= f"Policy with ID: {policy_id} retrieved successfully!",
                status_code= HTTPStatus.OK, data=result,
            )
            
    # return {
    #         "message": f"Policy with ID: {policy_id} retrieved successfully!",
    #         "status_code": HTTPStatus.OK,
    #         'data': result,
    #     }