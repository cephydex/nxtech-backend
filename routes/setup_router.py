from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi import Request
from http import HTTPStatus
from utils.exception_handler import *
from utils.cjwt import JWTBearer
from utils.file_uploader import *
from schemas.Resp import GenResponse
from repos.nat_n_dept import DepartmentRepo, NationalityRepo
from repos.title import TitleRepo
from schemas.Department import DepartmentCreate, DepartmentResult
from schemas.Title import TitleCreate, TitleResult
from repos.agent_n_bizintroducer import AgentRepo
from repos.biz_introducer import BizIntroducerRepo
from schemas.Agent import AgentCreate, AgentResult
from schemas.BizIntroducer import BizIntroducerCreate, BizIntroducerResult
from schemas.Profession import ProfessionCreate, ProfessionResult, ProfessionalGroupCreate, ProfessionalGroupResult
from repos.profession_n_group import ProfessionalGroupRepo, ProfessionRepo
import logging, traceback
from schemas.Resp import GenResponse
from repos.bank import BankRepo
from repos.user import UserRepo

logger = logging.getLogger(__name__)

router = APIRouter(
            prefix='/setup',
            tags=['Setup'],
            responses={422: {"message": "Request failed"}}
        )

auth_bearer = JWTBearer()


@router.get("/departments")
def get_department_list(request:Request, token:str=Depends(auth_bearer)):
    result = DepartmentRepo.fetch_all()
    
    return {
            "message": "Departments retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/users/min")
def get_user_list(request:Request, token:str=Depends(auth_bearer)):
    result = UserRepo.fetch_all_min()
    
    return {
            "message": "Departments retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.post("/departments")
async def create_department(req_data:DepartmentCreate, request:Request, token:str=Depends(auth_bearer)):
    result = await DepartmentRepo.create(req_data)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    
    msg = "Department created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Department could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg,
                status_code=code, 
                data=res_data,
            )


@router.get("/nationalities")
def get_nationality_list(request:Request, token:str=Depends(auth_bearer)):
    result = NationalityRepo.fetch_all()

    return {
            "message": "Nationalities retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/titles")
def get_title_list(request:Request, token:str=Depends(auth_bearer)):
    result = TitleRepo.fetch_all()
    
    return {
            "message": "Titles retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.post("/titles")
async def create_title(req_data:TitleCreate, request:Request, token:str=Depends(auth_bearer)):
    result = await TitleRepo.create(req_data)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    
    msg = "Title created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Title could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg,
                status_code=code, 
                data=result,
            )


@router.get("/banks")
def get_bank_list(request:Request, token:str=Depends(auth_bearer)):
    result = BankRepo.fetch_all()
    
    return {
            "message": "Banks retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/banks/{id}")
def get_bank_list(id: str, request:Request, token:str=Depends(auth_bearer)):
    result = BankRepo.fetch_by_id(id)
    print('1 Bank', result)
    
    return {
            "message": f"Banks with {id} retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


# @router.post("/titles")
# async def create_title(req_data:TitleCreate, request:Request, token:str=Depends(auth_bearer)):
#     result = await TitleRepo.create(req_data)
#     res_data = result["data"] if result["data"] else None
#     logger.warning(res_data)
    
#     msg = "Title created successfully!"
#     code = HTTPStatus.CREATED
#     if not res_data or not res_data['created_at']:
#         msg = "Title could not be created."
#         code = HTTPStatus.BAD_REQUEST

#     if result["errors"]:
#         res_data = result["errors"]
    
#     return GenResponse(
#                 message=msg,
#                 status_code=code, 
#                 data=result,
#             )


# @router.get("/agents")
# def get_agent_list(request:Request, token:str=Depends(auth_bearer)):
#     result = AgentRepo.fetch_all()
    
#     return {
#             "message": "Agent(s) retrieved successfully!",
#             "status_code": HTTPStatus.OK,
#             'data': result,
#         }


# @router.get("/agents/min")
# def get_agent_min_list(request:Request, token:str=Depends(auth_bearer)):
#     result = AgentRepo.fetch_min()
    
#     return {
#             "message": "Business Introducer(s) minimum retrieved successfully!",
#             "status_code": HTTPStatus.OK,
#             'data': result,
#         }


# @router.post("/agents")
# async def create_agent(req_data:AgentCreate, request:Request, token:str=Depends(auth_bearer)):
#     result = await AgentRepo.create(req_data)
#     res_data = result["data"] if result["data"] else None
#     logger.warning(res_data)
    
#     msg = "Agent created successfully!"
#     code = HTTPStatus.CREATED
#     if not res_data or not res_data['created_at']:
#         msg = "Agent could not be created."
#         code = HTTPStatus.BAD_REQUEST

#     if result["errors"]:
#         res_data = result["errors"]
    
#     return GenResponse(
#                 message=msg,
#                 status_code=code, 
#                 data=result,
#             )


@router.get("/biz-introducers")
def get_biz_introducer_list(request:Request, token:str=Depends(auth_bearer)):
    result = BizIntroducerRepo.fetch_all()
    
    return {
            "message": "Business Introducer(s) retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/biz-introducers/min")
def get_biz_introducers_min_list(request:Request, token:str=Depends(auth_bearer)):
    result = BizIntroducerRepo.fetch_min()
    
    return {
            "message": "Business Introducer(s) minimum retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


def validate_fields(vals: BizIntroducerCreate):
    val_str = ''
    if vals.itype == "Company":
        missing_fields = []
        if vals.business_name == 'string':
            missing_fields.append("business_name")
        if vals.business_reg_no == 'string':
            missing_fields.append("business_reg_no")
        if vals.primary_contact == 'string':
            missing_fields.append("primary_contact")
        if vals.tin_no == 'string':
            missing_fields.append("tin_no")
        if missing_fields:
            # raise ValueError(f"Missing required fields for Corporate account: {', '.join(missing_fields)}")
            val_str = f"Missing required fields for Corporate account: {', '.join(missing_fields)}"
        # return missing_fields
        
    elif vals.itype == "Individual":
        logger.debug('validate individual')
        missing_fields = []
        if vals.title_id == 'string':
            missing_fields.append("title_id")
        if vals.full_name == 'string':
            missing_fields.append("full_name")
        if vals.id_type == 'string':
            missing_fields.append("id_type")
        if vals.id_number == 'string':
            missing_fields.append("id_number")
        if missing_fields:
            val_str = f"Missing required fields for Individual account: {', '.join(missing_fields)}"
            # raise ValueError(f"Missing required fields for Individual account: {', '.join(missing_fields)}")
    return val_str

from utils.str import fmtPhoneNumber, getNextMemberId
@router.post("/biz-introducers")
async def create_biz_introducer(req_d:BizIntroducerCreate, request:Request, token:str=Depends(auth_bearer)):
    user_id = auth_bearer.get_user_id(token)
    logger.debug('Create biz intro')
    # logger.debug(req_d)
    req_d.contact_no = fmtPhoneNumber(req_d.contact_no)
    req_d.user_id = user_id

    validation = validate_fields(req_d)
    if validation != '':
        return GenResponse(
                message=validation,
                status_code=401, 
                data=None,
            )
    logger.debug(validation)

    result = await BizIntroducerRepo.create(req_d)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    
    msg = "Business Introducer created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Business Introducer could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg,status_code=code, data=result,
            )


# @router.delete("/biz-introducers/{id}")
# async def delete_biz_introducer(id: str, token:str=Depends(auth_bearer)):
#     result = await BizIntroducerRepo.delete(id)
    
#     return {
#             "message": "Business Introducer deleted successfully!",
#             "status_code": HTTPStatus.OK,
#             'data': result,
#         }

from repos.prospect import ProspectRepo, ProspectStageRepo
from schemas.Prospect import ProspectCreate, ProspectResult, ProspectStageCreate
@router.post("/prospects")
async def create_prospect(req_d:ProspectCreate, request:Request, token:str=Depends(auth_bearer)):
    userId = auth_bearer.get_user_id(token)
    req_d.created_by = str(userId)
    req_d.contact_no = fmtPhoneNumber(req_d.contact_no)

    result = await ProspectRepo.create(req_d)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    if res_data:
        psc = ProspectStageCreate
        psc.prospect_id = res_data["id"]
        psc.stage = req_d.stage
        psc.notes = req_d.notes
        # add prospect stage
        ps_rs = await ProspectStageRepo.create(psc)
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


@router.get("/prospects")
def get_prospect_list(request:Request, token:str=Depends(auth_bearer)):
    result = ProspectRepo.fetch_all()
    
    return {
            "message": "Prospects(s) retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }

@router.post("/prospect-stages")
async def create_prospect_stage(req_d:ProspectStageCreate, token:str=Depends(auth_bearer)):
    result = await ProspectStageRepo.create(req_d)
    logger.warning(result)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    # if res_data:
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

@router.get("/prospect-stages/{prospect_id}")
def get_prospect_stage_list(prospect_id:str, token:str=Depends(auth_bearer)):
    result = ProspectStageRepo.fetch_by_prospect(prospect_id)
    
    return {
            "message": "Prospect stage(s) retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


from repos.client import ClientRepo, ClientContactRepo
from schemas.Client import ClientCreate, ClientContactCreate
from utils.str import fmtPhoneNumber
@router.post("/clients")
async def create_client(req_d:ClientCreate, request:Request, token:str=Depends(auth_bearer)):
    userId = auth_bearer.get_user_id(token)
    req_d.created_by = str(userId)

    clientId = getNextMemberId()
    req_d.client_code = clientId
    req_d.contact_no = fmtPhoneNumber(req_d.contact_no)

    result = await ClientRepo.create(req_d)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    
    msg = "Client created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Client could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg,
                status_code=code, 
                data=result,
            )


@router.get("/clients")
def get_client_list(request:Request, token:str=Depends(auth_bearer)):
    result = ClientRepo.fetch_all()
    
    return {
            "message": "Client(s) retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/clients/{id}")
async def get_client(id: str, token:str=Depends(auth_bearer)):
    result = ClientRepo.fetch_by_id(id)
    
    return {
            "message": "Client retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.post("/client-contacts")
async def create_client_contact(client_id: str,req_d:ClientContactCreate, request:Request, token:str=Depends(auth_bearer)):
    req_d.client_id = client_id
    req_d.contact_no = fmtPhoneNumber(req_d.contact_no)

    client = ClientRepo.fetch_by_id(client_id)
    # logger.debug(client)
    # logger.debug(client['client_type'])
    if not client or client['client_type'] == 'Individual':
        return GenResponse(
                message="The selected client is not of type Corporate",
                status_code=HTTPStatus.OK, data=None,
            )

    result = await ClientContactRepo.create(req_d)
    res_data = result["data"] if result["data"] else None
    # logger.warning(res_data)
    
    msg = "Client contact created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Client contact could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg,
                status_code=code, 
                data=result,
            )


@router.get("/client-contacts")
def get_client_contact_list(request:Request, token:str=Depends(auth_bearer)):
    result = ClientContactRepo.fetch_all()

    return GenResponse(
                message="Client contact(s) retrieved successfully!",
                status_code=HTTPStatus.OK, 
                data=result,
            )


@router.get("/client-contacts/{client_id}")
async def get_client(client_id: str, token:str=Depends(auth_bearer)):
    result = ClientContactRepo.fetch_by_client_id(client_id)
    
    return GenResponse(
                message="Client contacts retrieved successfully!",
                status_code=HTTPStatus.OK, 
                data=result,
            )

# from schemas.ProspectionStage import ProspStageCreate
# from repos.pospection_stage import ProspectionStageRepo
# @router.post("/prospects")
# async def create_prospection_stage(req_d:ProspStageCreate, request:Request, token:str=Depends(auth_bearer)):
#     user_id = auth_bearer.get_user_id(token)
#     req_d.user_id = user_id
#     result = await ProspectionStageRepo.create(req_d)
#     res_data = result["data"] if result["data"] else None
#     # logger.warning(res_data)
    
#     msg = "Prospecting stage created successfully!"
#     code = HTTPStatus.CREATED
#     if not res_data or not res_data['created_at']:
#         msg = "Prospecting stage could not be created."
#         code = HTTPStatus.BAD_REQUEST

#     if result["errors"]:
#         res_data = result["errors"]
    
#     return GenResponse(
#                 message=msg,
#                 status_code=code, 
#                 data=result,
#             )


# @router.get("/prospects")
# def get_prospect_stage__list(request:Request, token:str=Depends(auth_bearer)):
#     result = ClientContactRepo.fetch_all()

#     return GenResponse(
#                 message="All Prospection stage(s) retrieved successfully!",
#                 status_code=HTTPStatus.OK, 
#                 data=result,
#             )


# @router.get("/prospects/client/{client_id}")
# async def get_prospect_stages_by_client(client_id: str, token:str=Depends(auth_bearer)):
#     result = ProspectionStageRepo.fetch_by_client_id(client_id)
    
#     return GenResponse(
#                 message="Prospection stage retrieved for client, was successfully!",
#                 status_code=HTTPStatus.OK, 
#                 data=result,
#             )


# @router.get("/prospects/user/{user_id}")
# async def get_prospect_stages_by_user(user_id: str, token:str=Depends(auth_bearer)):
#     result = ProspectionStageRepo.fetch_by_user_id(user_id)
    
#     return GenResponse(
#                 message="Prospection stage retrieved for user, was successfully!",
#                 status_code=HTTPStatus.OK, 
#                 data=result,
#             )


# @router.get("/prospects/user")
# async def get_prospect_stages_by_loggedin_user(token:str=Depends(auth_bearer)):
#     user_id = auth_bearer.get_user_id(token)
#     result = ProspectionStageRepo.fetch_by_user_id(user_id)
    
#     return GenResponse(
#                 message="Prospection stage retrieved for user, was successfully!",
#                 status_code=HTTPStatus.OK, 
#                 data=result,
#             )


# @router.get("/prospects")
# async def get_all_prospects(token:str=Depends(auth_bearer)):
#     # user_id = auth_bearer.get_user_id(token)
#     result = ProspectionStageRepo.fetch_all()
    
#     return GenResponse(
#                 message="All Prospection stage(s) retrieved successfully!",
#                 status_code=HTTPStatus.OK, 
#                 data=result,
#             )

@router.get("/clients/{id}")
async def get_client(id: str, token:str=Depends(auth_bearer)):
    result = ClientRepo.fetch_by_id(id)
    
    return {
            "message": "Client retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/prof-groups")
def get_professional_group_list(request:Request, token:str=Depends(auth_bearer)):
    result = ProfessionalGroupRepo.fetch_all()
    
    return {
            "message": "Professional Group(s) retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.post("/prof-groups")
async def create_professional_group(req_data:ProfessionalGroupCreate, request:Request, token:str=Depends(auth_bearer)):
    result = await ProfessionalGroupRepo.create(req_data)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    
    msg = "Professional group created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Professional group could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg,
                status_code=code, 
                data=result,
            )


@router.delete("/prof-groups/{id}")
async def delete_professional_group(id: str, token:str=Depends(auth_bearer)):
    result = await ProfessionalGroupRepo.delete(id)
    
    return {
            "message": "Professional group deleted successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/professions")
def get_professional_list(request:Request, token:str=Depends(auth_bearer)):
    result = ProfessionRepo.fetch_all()
    
    return {
            "message": "Profession(s) retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/professions/min")
def get_professions_min_list(request:Request, token:str=Depends(auth_bearer)):
    result = ProfessionRepo.fetch_min()
    
    return {
            "message": "Profession(s) minimum retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.post("/professions")
async def create_profession(req_data:ProfessionCreate, request:Request, token:str=Depends(auth_bearer)):
    result = await ProfessionRepo.create(req_data)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    
    msg = "Profession created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Profession could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg,
                status_code=code, 
                data=result,
            )


@router.delete("/professions/{id}")
async def delete_profession(id: str, token:str=Depends(auth_bearer)):
    result = await ProfessionRepo.delete(id)
    
    return {
            "message": "Profession deleted successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }



