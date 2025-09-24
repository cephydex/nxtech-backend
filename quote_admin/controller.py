from fastapi import APIRouter, Depends
import logging
import json
from utils.cjwt import JWTBearer
from http import HTTPStatus
from schemas.Resp import GenResponse
from typing import List
from repos.quote import QuoteExtraRepo, QuoteRepo
from schemas.Quote import QuoteCreate
from schemas.QuoteExtra import QuoteExtraCreate
# from .model import PolicyCreate
# from .service import PolicyRepo


logger = logging.getLogger(__name__)
router = APIRouter(
            prefix='/func',
            tags=['Func'],
            responses={422: {"message": "Request failed"}}
        )

auth_bearer = JWTBearer()


@router.post("/quotes")
async def create_quote(req_d:QuoteCreate, token:str=Depends(auth_bearer)):
    # userId = auth_bearer.get_user_id(token)
    req_d.created_by = auth_bearer.get_user_id(token)
    result = await QuoteRepo.create(req_d)
    logger.warning(result)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    # if res_data:
    msg = "Quote created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Quote could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg, data=result, status_code=code, 
            )


@router.get("/quotes")
def get_all_quotes(token:str=Depends(auth_bearer)):
    result = QuoteRepo.fetch_all()
    
    return GenResponse(
                message="Quotes retrieved successfully!",
                status_code=HTTPStatus.OK, data=result,
            )


@router.get("/quotes/project/{project_id}")
def get_all_quotes_for_a_project(project_id: str, token:str=Depends(auth_bearer)):
    result = QuoteRepo.fetch_by_project_id(project_id)
    
    return GenResponse(
                message=f"Quotes for project: {project_id} retrieved successfully!",
                status_code=HTTPStatus.OK, data=result,
            )

@router.post("/quote-extras")
async def create_quote_extras(req:QuoteExtraCreate, token:str=Depends(auth_bearer)):
    req.created_by = auth_bearer.get_user_id(token)
    req.extras = json.dumps(req.extras)
    result = await QuoteExtraRepo.create(req)
    res_data = result["data"] if result["data"] else None
    
    msg = "Quote extra(s) created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not len(res_data) >= 0:
        msg = "Quote extra(s) could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg, data=result, status_code=code, 
            )

@router.post("/quotes/{quote_id}/quote-extras")
async def create_quote_extras_by_quote(quote_id:str, req:QuoteExtraCreate, token:str=Depends(auth_bearer)):
    req.created_by = auth_bearer.get_user_id(token)
    req.quote_id = quote_id
    req.extras = json.dumps(req.extras)
    result = await QuoteExtraRepo.create(req)
    res_data = result["data"] if result["data"] else None
    
    msg = "Quote extra(s) created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not len(res_data) >= 0:
        msg = "Quote extra(s) could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg, data=result, status_code=code, 
            )


@router.post("/quotes/{quote_id}/multiple/quote-extras")
async def create_multiple_quote_extras_by_quote(quote_id:str, req:List[QuoteExtraCreate], token:str=Depends(auth_bearer)):
    req[0].created_by = auth_bearer.get_user_id(token)
    print("REQ", req)
    result = await QuoteExtraRepo.create_multiple(quote_id, req)
    res_data = result["data"] if result["data"] else None
    
    msg = "Quote extra(s) created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not len(res_data) >= 0:
        msg = "Quote extra(s) could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg, data=result, status_code=code, 
            )


@router.put("/quotes/{quote_id}/quote-extras/{ins_company_id}")
async def update_quote_extras_by_quote(quote_id:str, ins_company_id:str, token:str=Depends(auth_bearer)):
    result = await QuoteExtraRepo.update_selected_extras(quote_id, ins_company_id)
    res_data = result["data"] if result["data"] else None
    
    msg = "Quote extra(s) updated successfully!"
    code = HTTPStatus.CREATED
    if not res_data:
        msg = "Quote extra(s) update could not be completed."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg, data=result, status_code=code, 
            )

@router.get("/quote-extras")
def get_all_quote_extras(token:str=Depends(auth_bearer)):
    result = QuoteExtraRepo.fetch_all()

    return GenResponse(
                message="Quote extra(s) retrieved successfully!",
                status_code=HTTPStatus.OK, data=result,
            )

@router.get("/quotes/{quote_id}/quote-extras")
def get_all_quote_extras_by_quote_id(quote_id:str, token:str=Depends(auth_bearer)):
    result = QuoteExtraRepo.fetch_by_quote_id(quote_id)

    return GenResponse(
                message="Quote extra(s) retrieved successfully!",
                status_code=HTTPStatus.OK, data=result,
            )
