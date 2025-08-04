from typing import List
import uuid, logging
from schemas.ProspectionStage import ProspStageCreate, ProspStageResult
from models.ProspectionStage import ProspectionStage
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)


class ProspectionStageRepo:
    
    q_builder = QueryBuilder(model=None).table("prospection_stages")
        
    async def create(e: ProspStageCreate):
        res = {'errors': {}, 'data': None,}

        try:
            db_item = ProspectionStage()
            # db_item.id=str(uuid.uuid4()),
            db_item.client_id=e.client_id,
            db_item.user_id=e.user_id,
            db_item.source=e.source,
            db_item.stage=e.stage,
            db_item.notes=e.notes,
            db_item.entry_date=e.entry_date,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Prospection stage %s already exists" % e.client_id+" | "+e.user_id+" | "+e.stage)
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


    def fetch_all() -> List[ProspStageResult]:
        result =  ProspectionStage.with_('client').all()
        
        return result.serialize()


    # def fetch_by_id(id: str) -> List[ProspStageResult]:
    #     result =  ClientContact.with_('client').find(id)

    #     return result.serialize()


    def fetch_by_client_id(client_id: str) -> List[ProspStageResult]:
        result =  ProspectionStage.where('client_id', client_id).get()

        return result.serialize()


    def fetch_by_user_id(user_id: str) -> List[ProspStageResult]:
        result =  ProspectionStage.where('user_id', user_id).get()

        return result.serialize()
    
