from typing import List
import uuid
import json
import logging
from .model import PolicyCreate, PolicyResult
from models.Policy import Policy
from masoniteorm.query import QueryBuilder
from admin_quote.service import QuoteRepo


logger = logging.getLogger(__name__)


class PolicyRepo:
    
    q_builder = QueryBuilder(model=None).table("policies")
        
    async def create(e: PolicyCreate):
        res = {'errors': {}, 'data': None,}
        
        try:
            item = Policy()
            item.id = str(uuid.uuid4())
            item.created_by = e.created_by
            item.quote_id = e.quote_id
            item.start_date = e.start_date
            item.expiry_date = e.expiry_date
            item.policy_type_id = e.policy_type_id
            item.quote_props = json.dumps(e.quote_props)
            item.quote_amount = e.quote_amount
            item.project_id = e.project_id
            item.insurance_company_id = e.insurance_company_id
            db_res = item.save()

            # update quote has_policy flag
            _ = QuoteRepo.update_has_policy_status(e.quote_id, True)
            
            # db_item = e.model_dump()
            # logger.debug("MODEL DUMP")
            # logger.debug(db_item)
            # db_item['id'] = str(uuid.uuid4())
            # logger.debug(db_item)
            # db_item['quote_props'] = json.dumps(e.quote_props)
            # db_res = Policy.create(db_item)
            res['data'] = db_res.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Policy %s already exists" % e.quote_id+" | ("+json.dumps(e.quote_props)+", "+e.expiry_date.strftime("%Y-%m-%d")+")")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res

    async def delete(id: str):
        result = Policy.find(id).delete()

        return result


    def fetch_all() -> List:
        result =  Policy\
            .with_('quote')\
                .all()
        
        return result.serialize()


    def fetch_by_id(id: str) -> List[PolicyResult]:
        tmp_result =  Policy\
                        .with_('quote')\
                            .find(id)
        result = tmp_result.serialize() if tmp_result else None
        return result


    def fetch_by_project_id(project_id: str) -> List[PolicyResult]:
        tmp_result =  Policy\
                        .with_('quote')\
                            .where('project_id', project_id)\
                                .get()
        result = tmp_result.serialize()
        return result