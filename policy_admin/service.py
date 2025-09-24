from typing import List
import uuid
import json
import logging

from schemas.Quote import QuoteCreate, QuoteResult
from models.Quote import Quote
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)


class PolicyRepo:
    
    q_builder = QueryBuilder(model=None).table("prospect")
        
    async def create(e: QuoteCreate):
        res = {'errors': {}, 'data': None,}
        
        try:
            db_item = e.model_dump()
            db_res = Quote.create(db_item)
            res['data'] = db_res.serialize()

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


    def fetch_by_project_id(project_id: str) -> List[QuoteResult]:
        tmp_result =  Quote\
                        .with_('prospect')\
                        .with_('quote_extras')\
                            .where('project_id', project_id)\
                                .get()
        result = tmp_result.serialize()
        return result