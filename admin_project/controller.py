import logging
# import traceback
from fastapi import APIRouter, Depends
from http import HTTPStatus
from utils.cjwt import JWTBearer
from .service import ProjectRepo, ProjectCreateMany
from schemas.Resp import GenResponse


logger = logging.getLogger(__name__)
router = APIRouter(
            prefix='/func',
            tags=['Func'],
            responses={422: {"message": "Request failed"}}
        )

auth_bearer = JWTBearer()


@router.get("/prospects/{prospect_id}/projects")
def get_project_under_a_prospect(prospect_id:str, token:str=Depends(auth_bearer)):
    result = ProjectRepo.fetch_by_prospect_id(prospect_id)
    
    return GenResponse(
                message="Prospect projects detail retrieved successfully!", 
                data=result, status_code=HTTPStatus.OK, 
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
