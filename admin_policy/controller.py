from .model import PolicyCreate, PolicyRequest
from .service import PolicyRepo
from fastapi import APIRouter, Request, Depends
import logging
from utils.cjwt import JWTBearer
from http import HTTPStatus
from schemas.Resp import GenResponse
from utils.lib import Utils
from admin_quote.service import QuoteRepo


logger = logging.getLogger(__name__)
router = APIRouter(
            prefix='/func',
            tags=['Func'],
            responses={422: {"message": "Request failed"}}
        )

auth_bearer = JWTBearer()


@router.post("/policies")
async def create_policy(req_d:PolicyRequest, request:Request, token:str=Depends(auth_bearer)):
    # 5e1abf7a-93d0-4e6c-9482-c07b972adaef

    # get specified quote and quote extras
    quote_with_extras = QuoteRepo.fetch_by_with_extras(req_d.quote_id)
    # logger.debug(quote_with_extras)
    extras = quote_with_extras.get('quote_extras', None)
    extra = None
    if quote_with_extras and len(extras) > 0:
        # logger.debug(extras)
        extra = [item for item in extras if item.get('accepted') == True]
        extra = extra[0] if len(extra) > 0 else None
        # logger.debug('LIST')
        # logger.debug(extra)

    # calculate expiry date
    new_expiry = Utils.calculate_month_addition(req_d.duration)
    logger.warning(f'{req_d.duration} LATER :: {new_expiry}')

    c_data = PolicyCreate
    c_data.created_by = str(auth_bearer.get_user_id(token))
    c_data.quote_id = req_d.quote_id
    c_data.start_date = req_d.start_date
    c_data.expiry_date = new_expiry # to be calculated
    c_data.policy_type_id = quote_with_extras['policy_type_id']
    c_data.quote_props = quote_with_extras['entry_data']
    c_data.quote_amount = extra.get('quote_amount')
    c_data.project_id = quote_with_extras['project_id']
    c_data.insurance_company_id = extra.get('insurance_company_id')
    logger.warning("C DATA")
    logger.warning(c_data)

    result = await PolicyRepo.create(c_data)
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
                message=msg, status_code=code, 
                data=result,
            )


@router.get("/policies/{policy_id}")
def get_policy_by_id(policy_id:str, token:str=Depends(auth_bearer)):
    result = PolicyRepo.fetch_by_id(policy_id)
    
    return GenResponse(
                message= f"Policy with ID: {policy_id} retrieved successfully!",
                status_code= HTTPStatus.OK, data=result,
            )


@router.get("/policies")
def get_all_policies(token:str=Depends(auth_bearer)):
    result = PolicyRepo.fetch_all()
    
    return GenResponse(
                message= "All Policies retrieved successfully!",
                status_code= HTTPStatus.OK, data=result,
            )
