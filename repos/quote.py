from typing import List
import uuid
import logging
from schemas.Quote import QuoteCreate, QuoteResult
from models.Quote import Quote
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class QuoteRepo:
    
    q_builder = QueryBuilder(model=None).table("prospect")
        
    async def create(e: QuoteCreate):
        res = {'errors': {}, 'data': None,}
        import json
        try:
            db_item = Quote()
            db_item.id=str(uuid.uuid4()),
            db_item.project_id= e.project_id,
            db_item.prospect_id= e.prospect_id,
            db_item.policy_type_id= e.policy_type_id,
            db_item.insurance_company_id= e.insurance_company_id,
            db_item.premium= e.premium,
            db_item.currency= e.currency,
            db_item.valid_until= e.valid_until,
            db_item.document_url= e.document_url,
            db_item.entry_data= json.dumps(e.entry_data),
            db_item.created_by= e.created_by,
            db_item.status= e.status,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Quote %s already exists" % e.project_id+" | ("+e.entry_data+", "+e.valid_until+")")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res

    async def delete(id: str):
        result = Quote.find(id).delete()

        return result


    def fetch_all() -> List[QuoteResult]:
        result =  Quote.all()
        # result =  Quote.with_('title').with_('stages').all()
        
        return result.serialize()


    def fetch_by_id(id: str) -> List[QuoteResult]:
        tmp_result =  Quote\
                        .with_('prospect')\
                            .find(id)
        result = tmp_result.serialize() if tmp_result else None
        return result
