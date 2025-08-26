from typing import List
import uuid, logging
from schemas.ProspectionStage import ProspectionStageCreate
from models.ProspectionStage import ProspectionStage
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)


class ProspectionStageRepo:
    
    q_builder = QueryBuilder(model=None).table("prospection_stages")
        
    async def create(d: ProspectionStageCreate):
        res = {'errors': {}, 'data': None,}

        try:
            db_item = ProspectionStage()
            db_item.client_id= d.project_id,
            db_item.user_id= d.created_by,
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
    
