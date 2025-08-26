from typing import List
import uuid
import logging
from schemas.Prospect import ProspectCreate, ProspectResult
from models.Prospect import Prospect
from schemas.Prospect import ProspectionStageCreate
from models.ProspectionStage import ProspectionStage
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class ProspectRepo:
    
    q_builder = QueryBuilder(model=None).table("prospect")
        
    async def create(e: ProspectCreate):
        res = {'errors': {}, 'data': None,}
        
        # client_type, company_name, address_loc, email, contact_no, is_existing, client_code, company_reg_no, year_of_inc, 
        # uploaded_doc, tin_no, active_status, notes, 
        # account_manager, claims_manager, created_by,
        # title_id, first_name, last_name, other_names, dob, sex, nationality_id, id_type, id_number, pep, 
        # residential_addr, postal_addr, professional_group_id, profession_id,

        try:
            db_item = Prospect()
            db_item.id=str(uuid.uuid4()),
            db_item.title_id=e.title_id,
            db_item.first_name=e.first_name,
            db_item.last_name=e.last_name,
            db_item.other_names=e.other_names,
            db_item.email=e.email,
            db_item.contact_no=e.contact_no,
            db_item.sex=e.sex,
            db_item.address_loc=e.address_loc,
            db_item.nationality_id=e.nationality_id,
            db_item.client_type=e.client_type,
            
            db_item.company_name=e.company_name,
            db_item.year_of_inc=e.year_of_inc,
            # db_item.stage=e.stage,
            db_item.source=e.source,
            db_item.active_status=e.active_status,
            db_item.created_by=e.created_by,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Prospect %s already exists" % e.client_type+" | ("+e.first_name+", "+e.last_name+")")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res

    async def delete(id: str):
        result = Prospect.find(id).delete()

        return result


    def fetch_all() -> List[ProspectResult]:
        result =  Prospect.with_('title').all()
        
        return result.serialize()


    def fetch_by_id(id: str) -> List[ProspectResult]:
        tmp_result =  Prospect.with_('title')\
                                .with_('nationality')\
                                .with_('stages')\
                                    .find(id)
        result = tmp_result.serialize() if tmp_result else None
        return result




class ProspectionStageRepo:
    
    q_builder = QueryBuilder(model=None).table("prospection_stages")
        
    async def create(d: ProspectionStageCreate):
        res = {'errors': {}, 'data': None,}

        try:
            db_item = ProspectionStage()
            db_item.project_id= d.project_id,
            db_item.created_by= d.created_by,
            db_item.stage= d.stage,
            db_item.notes= d.notes,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Prospection stage %s already exists" % d.project_id+" | "+d.stage)
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res
    
        # client_type, company_name, address_loc, email, contact_no, is_existing, client_code, company_reg_no, year_of_inc, 
        # uploaded_doc, tin_no, active_status, notes, 
        # account_manager, claims_manager, created_by,
        # title_id, first_name, last_name, other_names, dob, sex, nationality_id, id_type, id_number, pep, 
        # residential_addr, postal_addr, professional_group_id, profession_id,


    async def delete(id: str):
        result = ProspectionStage.find(id).delete()

        return result


    def fetch_all() -> List:
        result =  ProspectionStage.with_('client').all()
        
        return result.serialize()


    def fetch_by_client_id(client_id: str) -> List:
        result =  ProspectionStage.where('client_id', client_id).get()

        return result.serialize()


    def fetch_by_user_id(user_id: str) -> List:
        result =  ProspectionStage.where('user_id', user_id).get()

        return result.serialize()
    



# from schemas.Prospect import ProspectStageCreate, ProspectResult
# from models.ProspectStage import ProspectStage
# class ProspectStageRepo:
#     q_builder = QueryBuilder(model=None).table("clients")
        
#     async def create(e: ProspectStageCreate):
#         res = {'errors': {}, 'data': None,}
        
#         try:
#             db_item = ProspectStage()
#             db_item.prospect_id=e.prospect_id,
#             db_item.stage=e.stage,
#             db_item.notes=e.notes,
#             db_item.save()
#             res['data'] = db_item.serialize()

#         except Exception as ex:
#             if 'unique constraint' in str(ex):
#                 logger.error("Prospect stage %s already exists" % e.client_code+" | "+e.client_type+" | ("+e.first_name+", "+e.last_name+")")
#                 res['errors']["unique_constraint"] = str(ex)
#             logger.error(str(ex))

#         return res
    

#     def fetch_by_prospect(prospect_id:str) -> List[ProspectResult]:
#         result =  ProspectStage.where('prospect_id', prospect_id).all()
        
#         return result.serialize()
