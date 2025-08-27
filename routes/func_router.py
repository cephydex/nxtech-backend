from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi import Request
from http import HTTPStatus
from utils.cjwt import JWTBearer
from schemas.Resp import GenResponse
import logging
import traceback
from utils.str import fmtPhoneNumber
from repos.prospect import ProspectRepo, ProspectionStageRepo
from schemas.Prospect import ProspectCreate, ProspectionStageCreate, ProspectCreateWProduct
from repos.project import ProjectCreate, ProjectRepo, ProjectCreateMany
from repos.product_column import ProductColumnRepo
from schemas.QuoteExtra import QuoteExtraRequest
from repos.quote import QuoteExtraRepo
from repos.quote import QuoteRepo, QuoteCreate

logger = logging.getLogger(__name__)
router = APIRouter(
            prefix='/func',
            tags=['Func'],
            responses={422: {"message": "Request failed"}}
        )

auth_bearer = JWTBearer()

@router.post("/prospects")
# async def create_prospect(req_d:ProspectCreate, request:Request, token:str=Depends(auth_bearer)):
async def create_prospect(req_d:ProspectCreateWProduct, request:Request, token:str=Depends(auth_bearer)):
    userId = auth_bearer.get_user_id(token)
    req_d.created_by = str(userId)
    req_d.contact_no = fmtPhoneNumber(req_d.contact_no)

    result = await ProspectRepo.create(req_d)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    if res_data:
        pj = ProjectCreate
        pj.prospect_id = res_data["id"]
        pj.policy_type_id = req_d.policy_type_id
        pj.created_by = str(userId)
        pj.status = req_d.stage
        p_res = await ProjectRepo.create(pj)

        psc = ProspectionStageCreate
        psc.created_by = str(userId)
        psc.project_id = p_res["data"]["id"]
        psc.prospect_id = res_data["id"]
        psc.stage = req_d.stage
        psc.notes = req_d.notes
        ps_rs = await ProspectionStageRepo.create(psc)
        logger.warning(ps_rs)
    
    msg = "Prospect created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Prospect could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg, data=result, status_code=code, 
            )


@router.post("/project/multiple")
async def create_multiple_projects(req_d:ProjectCreateMany, token:str=Depends(auth_bearer)):
    req_d.created_by = str(auth_bearer.get_user_id(token))

    result = await ProjectRepo.create_multiple(req_d)
    res_data = result["data"] if result["data"] else None
    logger.warning('MULTI RES')
    # logger.warning(result)
        
    msg = "Multiple project(s) created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not len(res_data) >= 0:
        msg = "Multiple project(s) could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg, data=result, status_code=code, 
            )


@router.get("/projects/gen")
def get_project_list_general(token:str=Depends(auth_bearer)):
    result = ProjectRepo.fetch_all_gen()

    return GenResponse(
                message="Project(s) retrieved successfully!", 
                data=result, status_code=HTTPStatus.OK, 
            )


@router.get("/projects/gen/prospect/{prospect_id}")
def get_project_list_general_by_prospect(prospect_id:str, token:str=Depends(auth_bearer)):
    result = ProjectRepo.fetch_all_gen_by_prospect(prospect_id)

    return GenResponse(
                message="Project(s) retrieved successfully!", 
                data=result, status_code=HTTPStatus.OK, 
            )

@router.get("/projects")
def get_project_list(token:str=Depends(auth_bearer)):
    result = ProjectRepo.fetch_all()

    return GenResponse(
                message="Project(s) retrieved successfully!", 
                data=result, status_code=HTTPStatus.OK, 
            )


@router.get("/projects/{id}")
def get_project_by_id(id:str, token:str=Depends(auth_bearer)):
    result = ProjectRepo.fetch_by_id(id)

    return GenResponse(
                message="Project(s) retrieved by ID successfully!", 
                data=result, status_code=HTTPStatus.OK, 
            )


@router.get("/prospects")
def get_prospect_list(token:str=Depends(auth_bearer)):
    result = ProspectRepo.fetch_all()

    return GenResponse(
                message="Prospect(s) retrieved successfully!", 
                data=result, status_code=HTTPStatus.OK, 
            )


@router.get("/prospects/{id}")
def get_prospect_by_id(id:str, token:str=Depends(auth_bearer)):
    result = ProspectRepo.fetch_by_id(id)
    
    return GenResponse(
                message="Prospect details retrieved successfully!", 
                data=result, status_code=HTTPStatus.OK, 
            )


@router.get("/prospects/{prospect_id}/projects")
def get_project_under_a_prospect(prospect_id:str, token:str=Depends(auth_bearer)):
    result = ProjectRepo.fetch_by_prospect_id(prospect_id)
    
    return GenResponse(
                message="Prospect projects detail retrieved successfully!", 
                data=result, status_code=HTTPStatus.OK, 
            )


@router.post("/prospect-stages")
async def create_prospect_stage(req_d:ProspectionStageCreate, token:str=Depends(auth_bearer)):
    result = await ProspectionStageRepo.create(req_d)
    logger.warning(result)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)

    msg = "Prospect stage created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Prospect stage could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg, data=result, status_code=code, 
            )

@router.get("/prospect-stages/{project_id}")
def get_prospect_stage_list(project_id:str, token:str=Depends(auth_bearer)):
    result = ProspectionStageRepo.fetch_by_project(project_id)
    
    return {
            "message": "Prospect stage(s) retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }



@router.get("/product-fields")
def get_all_product_fields(request:Request, 
    # token:str=Depends(auth_bearer)
):
    result = ProductColumnRepo.fetch_all()
    print('Product column', result)
    
    return {
            "message": f"Banks with {id} retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/product-fields/{id}")
def get_product_specific_field(id: str, request:Request, 
    # token:str=Depends(auth_bearer)
):
    result = ProductColumnRepo.fetch_by_id(id)
    print('Product column', result)
    
    return {
            "message": f"Product fields with {id} retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


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
                status_code=HTTPStatus.OK, 
                data=result,
            )


@router.post("/quote-extras")
async def create_quote_extras(req_d:QuoteExtraRequest, token:str=Depends(auth_bearer)):
    result = await QuoteExtraRepo.create(req_d)
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

@router.get("/quote-extras")
def get_all_quote_extras(token:str=Depends(auth_bearer)):
    result = QuoteExtraRepo.fetch_all()

    return GenResponse(
                message="Quote extra(s) retrieved successfully!",
                status_code=HTTPStatus.OK, data=result,
            )

# from repos.client import ClientRepo, ClientContactRepo
# from schemas.Client import ClientCreate, ClientContactCreate
# from utils.str import fmtPhoneNumber
# @router.post("/clients")
# async def create_client(req_d:ClientCreate, request:Request, token:str=Depends(auth_bearer)):
#     userId = auth_bearer.get_user_id(token)
#     req_d.created_by = str(userId)

#     clientId = getNextMemberId()
#     req_d.client_code = clientId
#     req_d.contact_no = fmtPhoneNumber(req_d.contact_no)

#     result = await ClientRepo.create(req_d)
#     res_data = result["data"] if result["data"] else None
#     logger.warning(res_data)
    
#     msg = "Client created successfully!"
#     code = HTTPStatus.CREATED
#     if not res_data or not res_data['created_at']:
#         msg = "Client could not be created."
#         code = HTTPStatus.BAD_REQUEST

#     if result["errors"]:
#         res_data = result["errors"]
    
#     return GenResponse(
#                 message=msg,
#                 status_code=code, 
#                 data=result,
#             )


# @router.get("/clients")
# def get_client_list(request:Request, token:str=Depends(auth_bearer)):
#     result = ClientRepo.fetch_all()
    
#     return {
#             "message": "Client(s) retrieved successfully!",
#             "status_code": HTTPStatus.OK,
#             'data': result,
#         }


# @router.get("/clients/{id}")
# async def get_client(id: str, token:str=Depends(auth_bearer)):
#     result = ClientRepo.fetch_by_id(id)
    
#     return {
#             "message": "Client retrieved successfully!",
#             "status_code": HTTPStatus.OK,
#             'data': result,
#         }

from schemas.Prospect import ProspectContactCreate
from repos.prospect import ProspectionStageRepo, ProspectRepo, ProspectContactRepo
@router.post("/prospects/{prospect_id}/contacts")
async def create_prospect_contact(
    prospect_id: str,
    req_d:ProspectContactCreate, 
    token:str=Depends(auth_bearer)
):
    req_d.contact_no = fmtPhoneNumber(req_d.contact_no)

    prospect = ProspectRepo.fetch_by_id(prospect_id)
    if not prospect or prospect['client_type'] == 'Individual':
        return GenResponse(
                message="The selected Prospect is not of type Corporate",
                status_code=HTTPStatus.OK, data=None,
            )
    # return {"all": "Oliver", "data": prospect}
    req_d.prospect_id = prospect_id
    result = await ProspectContactRepo.create(req_d)
    # result = None
    res_data = result["data"] if result["data"] else None
    # logger.warning(res_data)
    
    msg = "Prospect contact created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Prospect contact could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg, status_code=code, data=result,
            )


@router.get("/prospects/{prospect_id}/contacts")
def get_propect_contact_list(prospect_id:str, token:str=Depends(auth_bearer)):
    result = ProspectContactRepo.fetch_by_prospect_id(prospect_id)

    return GenResponse(
                message="Prospect contact(s) retrieved successfully!",
                status_code=HTTPStatus.OK, 
                data=result,
            )


@router.get("/prospects/contacts/all")
async def get_all_prospect_contacts(token:str=Depends(auth_bearer)):
    result = ProspectContactRepo.fetch_all()
    
    return GenResponse(
                message="All Prospect contacts retrieved successfully!",
                status_code=HTTPStatus.OK, 
                data=result,
            )
