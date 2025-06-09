from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi import status, Request
import logging, os
from utils.exception_handler import *
from utils.cjwt import (JWTBearer, get_password_hash)
from schemas.Auth import RoleCreate
from typing import List


router = APIRouter(
            prefix='/admin',
            tags=['Admin'],
            responses={422: {"message": "Request failed"}}
        )

adm_bearer = JWTBearer()
from http import HTTPStatus
from repos.auth import RoleRepo, AdminRepo, InstRepo
from schemas.Auth import RoleCreate, AdminCreate, InstCreate, InstResult
# from schemas.musiga.Member import MemberCreate, UpdateStatusRequest
from repos.member import MemberRepo
from repos.musiga.mem_educ_n_contact import MemberEducRepo, RelatedContactRepo

from repos.musiga.event_n_performance import EventRepo, LivePerformanceRepo
from schemas.musiga.EventType import EventTypeCreate
from schemas.musiga.LivePerformance import LivePerformanceCreate, LivePerformanceArtiste as LivePerfArtisteSchema
from repos.musiga.grant_n_project import GrantAndFimRepo, GrantAndFimCreate
from repos.musiga.project import ProjectRepo, ProjectCreate
from schemas.musiga.MemberExtra import ArtisticProfileCreate, ExtraInfoCreate
from repos.musiga.member_extra import ArtisticProfileRepo, ExtraInfoRepo


logger = logging.getLogger(__name__)


@router.get("/roles")
async def get_all_roles(
    request:Request,
    token:str = Depends(adm_bearer),
):
    res = RoleRepo.fetch_all()
    # print("Roles", res)

    return {
        "message": "All roles retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": res
    }


@router.post("/roles")
async def create_new_role(
    request:Request,
    req: RoleCreate,
    token:str = Depends(adm_bearer), 
):
    res = await RoleRepo.create(req)
    # print("Dict", res.as_dict())
    
    msg = "Role created successfully!"
    code = HTTPStatus.CREATED
    if not hasattr(res,'created_at'):
        msg = "Role could not be created."
        code = HTTPStatus.BAD_REQUEST

    return {
        "message": msg,
        "status_code": code,
        "data": res.as_dict()
    }

from repos.musiga.title_region_n_music_role import TitleRepo, MusicRoleRepo, RegionRepo
from schemas.musiga.MiscSchema import TitleCreate
@router.get("/titles")
async def get_all_titles(
    request:Request,
    # token:str = Depends(adm_bearer),
):
    res = TitleRepo.fetchAll()

    return {
        "message": "All titles retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": res
    }


@router.post("/titles")
async def create_title(
    request:Request,
    req_data: TitleCreate,
    token:str=Depends(adm_bearer), 
):
    res = await TitleRepo.create(req_data)
    res_data = res["data"] if res["data"] else None
    logger.warning(res_data)
    
    msg = "Title created successfully!"
    code = HTTPStatus.CREATED
    if not res_data:
        msg = "Title could not be created."
        code = HTTPStatus.BAD_REQUEST

    if res["errors"]:
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


@router.delete("/titles/{id}")
async def delete_title(
    id: str,
    request:Request,
    token:str=Depends(adm_bearer), 
):
    res = await TitleRepo.delete(id)
    res_error = res["errors"] if res["errors"] else None
    logger.warning(res_error)
        
    msg = "Title deleted successfully!"
    code = HTTPStatus.OK
    if res_error:
        msg = "Title could not be deleted."
        code = HTTPStatus.BAD_REQUEST

    return {
        "message": msg,
        "status_code": code,
        "data": res_error
    }


@router.get("/regions")
async def get_all_regions(
    request:Request,
    # token:str = Depends(adm_bearer),
):
    res = RegionRepo.fetchAll()

    return {
        "message": "All regions retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": res
    }


@router.get("/music-roles")
async def get_all_music_roles(
    request:Request,
    # token:str = Depends(adm_bearer),
):
    res = MusicRoleRepo.fetchAll()

    return {
        "message": "All music roles retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": res
    }

@router.post("/register")
async def register_admin(
    request:Request,
    req: AdminCreate,
):
    logger.warning("REQ :: %s " % str(req))
    hash_pwd = get_password_hash(req.password)
    req.password = hash_pwd
    res = await AdminRepo.create(req)
    res_data = res["data"].serialize() if res["data"] else None
    logger.warning(res_data)
    msg = "Admin registration could not be completed."
    code = HTTPStatus.BAD_REQUEST
    # if hasattr(res_data, 'created_at'):
    if res_data and res_data['created_at']:
        msg = "Admin registration completed successfully!"
        code = HTTPStatus.CREATED
    
    if res["errors"]:
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


import traceback
from .services import prep_xlsx_file, getNextMemberId, processAllName
from .services import getNextMemberId
from repos.musiga.title_region_n_music_role import RegionRepo

@router.post("/members")
async def add_new_member(
    request:Request,
    req: MemberCreate,
    token: str = Depends(adm_bearer),
):
    
    # add image to s3 bucket if image_url is not empty
    req.image_url = None
    # req.passport_image = None
    if req.image_url and req.image_url != "":
        logger.warning("Member image provided but not yet uploaded")
        pass
        
    # last_member = MemberRepo.get_last_member_id()
    # print("Members ORD", last_member)
    member_id = getNextMemberId()

    user_id = adm_bearer.get_user_id(token)
    req.created_by = str(user_id)
    req.member_id = member_id

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


@router.post("/members/bulk")
async def process_bulk_member_data(file: UploadFile, token:str=Depends(adm_bearer)):
    
    if not file.filename.endswith('.csv') and not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="Only CSV and XLSX file(s) are allowed")

    # if file.filename.endswith('.csv') or file.filename.endswith('.xlsx'):
    if file.filename.endswith('.xlsx'):
        df = await prep_xlsx_file(file)
        
    try:        
        # role_res = RoleRepo.find_by_name(db, 'performer')
        # role_id = role_res.id
        sel_list = [
                    "Singer", "Arranger", "Composer/Author", 
                    "Producer", "Other", "Performer", 
                    "Instrumentalist", "Teacher",
                ]
        role_list = MusicRoleRepo.fetchWithList(sel_list)
        print("Role List", role_list)

        err_msgs = []
        data_size = len(df)
        for i, item in enumerate(df):
            if i == 0:
                continue
            
            try:
                # print("DATA", item)
                user_id = str(adm_bearer.get_user_id(token))
                all_names = item[0]            
                first_name, other_names = processAllName(all_names)
                surname_tmp = item[1]
                stage_name_tmp= item[2] if item[2] != '' else None
                
                sex = "male" if item[9] == "M" else "female"
                contact_no = str(item[13])
                email_tmp = item[14]
                dob_tmp = str(item[10]) if item[10] else None
                # process region
                region_tmp = "Greater Accra" if "accra" in str(item[15]).lower() else item[15]
                reg_res = RegionRepo.fetchByName(region_tmp)
                # print("DB REG", reg_res)
                region_tmp = reg_res[0].get("id") if reg_res else "00000000-0000-4000-0000-c00100000000"

                title_id = "00000000-0000-4000-8000-a10000000000" if sex == 'male' else "00000000-0000-4000-8000-a30000000000"
                
                print("RET #%d | FN %s | LN: %s | ON %s | STG %s | SEX %s | TEL %s | EMAIL %s | DOB %s | REGION %s" % 
                        (i, first_name, surname_tmp, other_names, stage_name_tmp, sex, contact_no, email_tmp, dob_tmp, region_tmp)
                    )

                # 0 full_name, 1 surname, 2 stage_name, 3 role, 4 composer/singer, 5 performer, 6 (Teacher, Arranger, Engg)
                # , 7 prof, 8 other, 9 sex, 10 dob, 12 phone, 13 email, 14 region, 14 membership_id
                # , 15 Exp. Date Orig, 16 Exp Date (F), 17 Expired, 18 Memb Cat, 19 New/Renewal, 20 Genre
                
                # insert data
                db_item = MemberCreate(
                    title = title_id,
                    surname = surname_tmp, 
                    first_name = first_name,
                    stage_name = stage_name_tmp,
                    other_names = other_names,
                    dob = dob_tmp,
                    sex = sex,
                    contact_no = contact_no,
                    whatsapp_no = contact_no,
                    email = email_tmp,
                    home_region = region_tmp,
                    hometown = "N/A",

                    marital_status = "single",
                    member_type = 'standard',
                    member_of_group = False,
                    languages_spoken = ["Twi", "English"],
                    image_url = None,
                    
                    # postal_addr
                    residential_addr = "N/A",
                    # social_security_no
                    # place_of_birth
                    # music_role = item[]
                    # music_role_other = item[]
                    # website: Optional[str] = None
                    # group_name: Optional[str] = None
                    # title:str
                    country_of_birth = "Ghanaian",
                    citizenship = "Ghanaian",
                    active_status = "active",
                    place_of_birth = "N/A",
                )
                
                db_item.created_by = str(user_id)
                # print("DB ITEM", db_item)
                if i == (data_size -1):
                    member_id = getNextMemberId()
                    db_item.member_id = member_id
                    mem_res = await MemberRepo.create(db_item)
                    print("CRT RES", mem_res)
                    pass
                
            except Exception as ex:
                traceback.print_exc()
                pass
            # print("Members ORD", member_id)
            # mem_res = await MemberRepo.create(req)

            # try:
            #     art_res = await ArtisteRepo.create(db, db_item)
            #     logger.warning("ENTRY :: RES")
            #     logger.warning(art_res)
            # except exc.IntegrityError as ie:
            #     logger.error("SQL ERR :: %s" % str(ie.orig))
            #     det = "(legal_name=%s, stage_name=%s)" % (db_item.legal_name, db_item.stage_name)
            #     if 'duplicate key' in str(ie.orig) and 'email' in str(ie.orig):
            #         err_msgs.append(f"Member email: {db_item.email} already exists | {det}")
            #     if 'duplicate key' in str(ie.orig) and 'national_id' in str(ie.orig):
            #         err_msgs.append(f"Member national ID: {db_item.national_id} already exists | {det}")
            #     if 'duplicate key' in str(ie.orig) and 'phone' in str(ie.orig):
            #         err_msgs.append(f"Member phone No.: {db_item.phone} already exists | {det}")
            #     db.rollback()

            # except exc.SQLAlchemyError as se:
            #     # error = str(se.__dict__['orig'])
            #     logger.error("SQL ERR :: %s" % str(se))

        # data = data_retrieved
        print("TOTAL LEN", len(df))
        msg = "Members' data uploaded successfully"
        if len(err_msgs) > 0:
            data = err_msgs
            msg = "Sorry, data could not be loaded successfully"

        return {
            "message": msg,
            "status_code": 200,
            "data": {}
        }
    
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/members")
async def get_all_members(
    request:Request,
    token:str=Depends(adm_bearer),
):
    res = MemberRepo.fetch_all_active()
    return {
        "message": "All MUSIGA members retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": res
    }


@router.get("/members/unapproved")
async def get_unapproved_members_list(
    request:Request,
    token:str=Depends(adm_bearer),
):
    res = MemberRepo.fetch_with_status('pending')
    return {
        "message": "All MUSIGA new entries retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": res
    }


@router.get("/members/status/{name}")
async def get_members_by_status(
    name: str,
    request: Request,
    token: str=Depends(adm_bearer),
):
    res = MemberRepo.fetch_with_status(name)
    return {
        "message": f"All MUSIGA entries with status({name}) retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": res
    }


@router.get("/members/{id}")
async def get_member_by_id(
    request:Request,
    id:str,
    token:str=Depends(adm_bearer),
):
    res = MemberRepo .fetch_by_id(id)

    return {
        "message": "MUSIGA member detail retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": res
    }


@router.put("/members/{id}/status")
async def get_member_by_id(
    request:Request,
    id:str,
    req: UpdateStatusRequest,
    token:str=Depends(adm_bearer),
):
    res = await MemberRepo.update_active_status(id, req)
    msg = "MUSIGA member active status updated successfully!"
    code = HTTPStatus.OK
    if res.get('errors'):
        errors = res.get('errors')
        msg = errors.get('msg')
        code = HTTPStatus.BAD_REQUEST
        res = errors.get('other')
        
    return {
        "message": msg,
        "status_code": code,
        "data": res
    }


@router.get("/members/region/{region}")
async def get_all_members_by_region(
    region:str, 
    request:Request,
    token:str=Depends(adm_bearer),
):
    res = MemberRepo.fetch_all_active_by_region(region)
    return {
        "message": "All MUSIGA members retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": res
    }


@router.get("/members/region_name/{region}")
async def get_all_members_by_region_name(
    region:str, 
    request:Request,
    token:str=Depends(adm_bearer),
):
    res = MemberRepo.fetch_all_active_by_region_name(region)
    return {
        "message": "All MUSIGA members retrieved successfully using region name!",
        "status_code": HTTPStatus.OK,
        "data": res
    }


@router.post("/members/{id}/add/extra-info")
async def add_extra_info_to_member(
    request:Request,
    id:str,
    req: List[ExtraInfoCreate],
    token: str = Depends(adm_bearer),
):
    res = await ExtraInfoRepo.create_bulk(req, id)
    logger.warning("EXTRA :: RES")
    logger.warning(res)

    code = HTTPStatus.CREATED
    msg = "Genre, Instruments or Collaborations was added successfully!"
    if res['errors']:
        code = HTTPStatus.FORBIDDEN
        msg = "Genre, Instruments or Collaborations could not be added"

    return {
        "message": msg,
        "status_code": code,
        "data": res
    }


@router.post("/members/{id}/add/artistic-profile")
async def add_extra_info_to_member(
    request:Request,
    id:str,
    req: List[ArtisticProfileCreate],
    token: str = Depends(adm_bearer),
):
    res = await ArtisticProfileRepo.create_bulk(req, id)
    logger.warning("ART :: RES")
    logger.warning(res)

    code = HTTPStatus.CREATED
    msg = "Awards and citations, Welfare intervention or Shows was added successfully"
    if res['errors']:
        code = HTTPStatus.FORBIDDEN
        msg = "Awards and citations, Welfare intervention or Shows could not be added"

    return {
        "message": msg,
        "status_code": code,
        "data": res
    }


@router.get("/event-types")
async def get_event_types(
    request:Request,
    # token:str=Depends(adm_bearer), 
):
    db_res = EventRepo.fetch_all()
    
    return {
        "message": "Event types retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }


@router.post("/event-types")
async def create_new_institution(
    request:Request,
    req_data: EventTypeCreate,
    token:str=Depends(adm_bearer), 
):
    res = await EventRepo.create(req_data)
    res_data = res["data"] if res["data"] else None
    logger.warning(res_data)
    
    msg = "Event type created successfully!"
    code = HTTPStatus.CREATED
    if not res_data['created_at']:
        msg = "Event type could not be created."
        code = HTTPStatus.BAD_REQUEST

    if res["errors"]:
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


@router.post("/live-performances")
async def create_new_live_performances(
    request:Request,
    req_data: LivePerformanceCreate,
    token:str=Depends(adm_bearer), 
):
    res = await LivePerformanceRepo.create(req_data)
    res_data = res["data"] if res["data"] else None
    logger.warning(res_data)
    
    msg = "Live performance created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Live performance could not be created."
        code = HTTPStatus.BAD_REQUEST

    if res["errors"]:
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


@router.post("/live-performances/{id}/add-artistes")
async def create_new_live_performances(
    request:Request,
    id: str,
    req_data: List[LivePerfArtisteSchema],
    token:str=Depends(adm_bearer), 
):
    res = await LivePerformanceRepo.add_artistes_bulk(req_data, id)
    # print("DB RES", res)
    logger.warning(res)
    res_data = res["data"] if res["data"] else None
    
    msg = "Addition of Artiste(s) to specified Live performance was successful!"
    code = HTTPStatus.CREATED
    # if not res_data or not res_data['created_at']:

    if res["errors"]:
        msg = "Addition of Artiste(s) to specified Live performance was not successful."
        code = HTTPStatus.BAD_REQUEST
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


@router.post("/live-performances/add-artistes")
async def create_new_live_performances(
    request:Request,
    # id: str,
    req_data: List[LivePerfArtisteSchema],
    token:str=Depends(adm_bearer), 
):
    res = await LivePerformanceRepo.add_artistes_bulk_orm(req_data)
    res_data = res["data"] if res["data"] else None
    logger.warning(res_data)
    
    msg = "Live performance created successfully!"
    code = HTTPStatus.CREATED
    # if not res_data or not res_data['created_at']:

    if res["errors"]:
        msg = "Live performance could not be created."
        code = HTTPStatus.BAD_REQUEST
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


@router.get("/live-performances")
async def get_live_performances(
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = LivePerformanceRepo.fetch_all()
    
    return {
        "message": "Live performance retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }


@router.get("/live-performances/artistes")
async def get_artistes_with_live_performances(
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = LivePerformanceRepo.fetch_performance_artistes_all()
    
    return {
        "message": "All Live performance and their artistes retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }


@router.get("/live-performances/{id}/artistes")
async def get_artistes_for_live_performance(
    id: str,
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = LivePerformanceRepo.fetch_performance_artistes_by_id(id)
    
    return {
        "message": "All Artistes for specified Live performance retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }


@router.post("/grants-and-fims")
async def create_new_grant_or_fim(
    request:Request,
    req_data: GrantAndFimCreate,
    token:str=Depends(adm_bearer), 
):
    res = await GrantAndFimRepo.create(req_data)
    res_data = res["data"] if res["data"] else None
    logger.warning(res_data)
    
    msg = "Grant or FIM created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Grant or FIM could not be created."
        code = HTTPStatus.BAD_REQUEST

    if res["errors"]:
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


@router.get("/grants-and-fims")
async def get_grants_or_fims(
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = GrantAndFimRepo.fetch_all()
    
    return {
        "message": "Grants/FIMS retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }


@router.post("/projects")
async def create_project(
    request:Request,
    req_data: ProjectCreate,
    token:str=Depends(adm_bearer), 
):
    user_id = adm_bearer.get_user_id(token)
    # req.created_by = str(user_id)
    req_data.created_by = str(user_id)
    res = await ProjectRepo.create(req_data)
    res_data = res["data"] if res["data"] else None
    logger.warning(res_data)
    
    msg = "Project created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Project could not be created."
        code = HTTPStatus.BAD_REQUEST

    if res["errors"]:
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


@router.get("/projects")
async def get_projects(
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = ProjectRepo.fetch_all()
    
    return {
        "message": "Projects retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }


from repos.musiga.dues_mgmt import DuePaymentRepo, DueSetupCreate, DueSetupRepo, DuePaymentCreate
@router.post("/dues/setups")
async def create_due_setups(
    request:Request,
    req_data: DueSetupCreate,
    token:str=Depends(adm_bearer), 
):
    user_id = adm_bearer.get_user_id(token)
    req_data.created_by = str(user_id)
    if not req_data.name:
        # from datetime import date
        # m_year = date.today().year
        req_data.name =  f"DUE_SETUP_{req_data.year}"
    res = await DueSetupRepo.create(req_data)
    res_data = res["data"] if res["data"] else None
    logger.warning(res_data)
    
    msg = "Due setup created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Due setup could not be created."
        code = HTTPStatus.BAD_REQUEST

    if res["errors"]:
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


@router.get("/dues/setups")
async def get_due_setups(
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = DueSetupRepo.fetch_all()
    
    return {
        "message": "Due setups retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }


@router.get("/dues/setups/{id}")
async def get_due_setups(
    id: str,
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = DueSetupRepo.fetch_by_id(id)
    
    return {
        "message": "Due setups retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }

from decimal import Decimal
@router.get("/dues/setups/{due_id}/member/{member_id}")
async def get_due_setup_and_payments_by_ids(
    due_id: str,
    member_id: str,
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = DuePaymentRepo.fetch_by_due_and_member_ids(due_id, member_id)
    data_extras = {}
    if db_res and len(db_res) > 0:
        due_amount = db_res[0]["due_setup"]["amount"]
        paid_amounts = [x.get("amount", 0) for x in db_res]
        data_extras["due_amount"] = due_amount
        
        total_paid = sum(map(Decimal, paid_amounts))
        data_extras["total_payments"] = total_paid
        # print("LEN", len(db_res), due_amount, paid_amounts, total_paid)
    
    return {
        "message": "Payment(s) for specified due setup and member retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res,
        "data_extras": data_extras,
    }


@router.post("/dues/payments")
async def create_due_payments(
    request:Request,
    req_data: DuePaymentCreate,
    token:str=Depends(adm_bearer), 
):
    user_id = adm_bearer.get_user_id(token)
    req_data.created_by = str(user_id)
    res = await DuePaymentRepo.create(req_data)
    res_data = res["data"] if res["data"] else None
    logger.warning(res_data)
    
    msg = "Due setup created successfully!"
    code = HTTPStatus.CREATED
    if not res_data or not res_data['created_at']:
        msg = "Due setup could not be created."
        code = HTTPStatus.BAD_REQUEST

    if res["errors"]:
        res_data = res["errors"]

    return {
        "message": msg,
        "status_code": code,
        "data": res_data
    }


@router.get("/dues/payments")
async def get_due_payments(
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = DuePaymentRepo.fetch_all()
    
    return {
        "message": "Due setups retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }


@router.get("/dues/member/{member_id}/payments")
async def get_due_payments_for_member(
    member_id: str,
    request:Request,
    token:str=Depends(adm_bearer), 
):
    db_res = DuePaymentRepo.fetch_by_member_id(member_id)
    
    return {
        "message": "Payment(s) for specified member retrieved successfully!",
        "status_code": HTTPStatus.OK,
        "data": db_res
    }
