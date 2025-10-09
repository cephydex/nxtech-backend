from typing import List
import uuid
import logging
import json
from .model import QuoteCreate, QuoteResult, QuoteExtraCreate
from models.Quote import Quote
from models.QuoteExtra import QuoteExtra
from masoniteorm.query import QueryBuilder


logger = logging.getLogger(__name__)

class QuoteRepo:
    
    q_builder = QueryBuilder(model=None).table("prospect")
        
    async def create(e: QuoteCreate):
        res = {'errors': {}, 'data': None,}
        import json
        try:
            db_item = Quote()
            db_item.id=str(uuid.uuid4())
            db_item.project_id= e.project_id
            db_item.prospect_id= e.prospect_id
            db_item.policy_type_id= e.policy_type_id
            db_item.insurance_company_id= e.insurance_company_id
            db_item.premium= e.premium
            db_item.currency= e.currency
            db_item.valid_until= e.valid_until
            db_item.document_url= e.document_url
            db_item.entry_data= json.dumps(e.entry_data)
            db_item.created_by= e.created_by
            db_item.status= e.status
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


    def fetch_by_with_extras(id: str) -> QuoteResult:
        tmp_result =  Quote\
                        .with_('quote_extras')\
                            .find(id)
        
        return tmp_result.serialize() if tmp_result else None


    def fetch_by_project_id(project_id: str) -> List[QuoteResult]:
        tmp_result =  Quote\
                        .with_('prospect')\
                        .with_('quote_extras')\
                            .where('project_id', project_id)\
                                .get()

        return tmp_result.serialize()


    def update_has_policy_status(id:str, has_policy:bool):
        res = {'errors': {}, 'data': None,}
        result = Quote.where('id', id)\
                    .update({"has_policy": has_policy})

        res['data'] = result.serialize()
        return res


class QuoteExtraRepo:
    
    async def create(e: QuoteExtraCreate):
        res = {'errors': {}, 'data': None,}
        try:
            q_data = e.model_dump()
            print('DATA', q_data)
            db_res = QuoteExtra.create(q_data)
            res['data'] = db_res.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error(f"Quote extras {e.quote_id} | ({e.extras}) already exists")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res
    
    
    async def create_multiple(quote_id: str, e: List[QuoteExtraCreate]):
        res = {'errors': {}, 'data': None,}
        q_data = []
        created_by = e[0].created_by

        try:
            for item in e:
                tmp = item.model_dump()
                tmp["quote_id"] = quote_id
                tmp["created_by"] = created_by
                tmp["extras"] = json.dumps(item.extras)
                q_data.append(tmp)

            db_res = QuoteExtra.bulk_create(q_data)
            res['data'] = db_res.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error(f"Quote extras for quote {quote_id} already exists")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res
    
    async def update_selected_extras(quote_id:str, ins_company_id:str):
        res = {'errors': {}, 'data': None,}
        result = QuoteExtra.where('quote_id', quote_id)\
            .where('insurance_company_id', ins_company_id)\
                .update({"accepted": True})
        # print("DET", result.serialize())
        res['data'] = result.serialize()
        return res

    def fetch_all() -> List[QuoteResult]:
        result =  QuoteExtra.all()
        # result =  Quote.with_('title').with_('stages').all()
        
        return result.serialize()

    def fetch_by_quote_id(quote_id:str) -> List:
        result =  QuoteExtra.where('quote_id', quote_id).all()
        
        return result.serialize()