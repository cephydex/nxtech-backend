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
from repos.agent_n_bizintroducer import AgentRepo, BizIntroducerRepo
from schemas.Agent import AgentCreate, AgentResult
from schemas.BizIntroducer import BizIntroducerCreate, BizIntroducerResult
from schemas.Profession import ProfessionCreate, ProfessionResult, ProfessionalGroupCreate, ProfessionalGroupResult
from repos.profession_n_group import ProfessionalGroupRepo, ProfessionRepo
import logging, traceback
from schemas.Resp import GenResponse

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
    
    # return GenResponse(
    #             message="Departments retrieved successfully!",
    #             status_code=HTTPStatus.OK, 
    #             data=result,
    #         )


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


@router.get("/agents")
def get_agent_list(request:Request, token:str=Depends(auth_bearer)):
    result = AgentRepo.fetch_all()
    
    return {
            "message": "Agent(s) retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.get("/agents/min")
def get_agent_min_list(request:Request, token:str=Depends(auth_bearer)):
    result = AgentRepo.fetch_min()
    
    return {
            "message": "Business Introducer(s) minimum retrieved successfully!",
            "status_code": HTTPStatus.OK,
            'data': result,
        }


@router.post("/agents")
async def create_agent(req_data:AgentCreate, request:Request, token:str=Depends(auth_bearer)):
    result = await AgentRepo.create(req_data)
    res_data = result["data"] if result["data"] else None
    logger.warning(res_data)
    
    msg = "Agent created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Agent could not be created."
        code = HTTPStatus.BAD_REQUEST

    if result["errors"]:
        res_data = result["errors"]
    
    return GenResponse(
                message=msg,
                status_code=code, 
                data=result,
            )


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


@router.post("/biz-introducers")
async def create_biz_introducer(req_data:BizIntroducerCreate, request:Request, token:str=Depends(auth_bearer)):
    result = await BizIntroducerRepo.create(req_data)
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
                message=msg,
                status_code=code, 
                data=result,
            )


@router.delete("/biz-introducers/{id}")
async def delete_biz_introducer(id: str, token:str=Depends(auth_bearer)):
    result = await BizIntroducerRepo.delete(id)
    
    return {
            "message": "Business Introducer deleted successfully!",
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
