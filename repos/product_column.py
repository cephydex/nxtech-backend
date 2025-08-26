from typing import List
import uuid, logging
# from schemas.PolicyType import PolicyTypeCreate, PolicyTypeResult
from models.ProductColumn import ProductColumn
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class ProductColumnRepo:
    
    q_builder = QueryBuilder(model=None).table("product_columns")
        
    # async def create(e: PolicyTypeCreate):
    #     res = {'errors': {}, 'data': None,}

    #     try:
    #         db_item = PolicyType()
    #         db_item.id=str(uuid.uuid4())
    #         db_item.cat_id=e.cat_id
    #         db_item.name=e.name
    #         db_item.description=e.description
    #         db_item.commission=e.commission
    #         # db_item.created_by=e.created_by,
    #         db_item.save()
    #         res['data'] = db_item.serialize()

    #     except Exception as ex:
    #         if 'unique constraint' in str(ex):
    #             logger.error("Policy type %s already exists" % e.name+" | ("+e.description+", "+e.commission+")")
    #             res['errors']["unique_constraint"] = str(ex)
    #         logger.error(str(ex))

    #     return res

    def fetch_all() -> List:
        result =  ProductColumn.all(["id", "data", ])
        
        return result.serialize()


    def fetch_by_id(id: str) -> List:
        # tmp_result =   ProductColumnRepo.q_builder.\
        #         statement(
        #             "SELECT * FROM public.product_columns WHERE data->>'product_id' = '00000000-0000-3000-8000-a10000000003'"
        #         )

        tmp_result =   ProductColumnRepo.q_builder.\
                statement(
                    "SELECT * FROM public.product_columns WHERE data->>'product_id' = '?'"
                , ['00000000-0000-3000-8000-a10000000003'])
        return tmp_result

        # SELECT * FROM public.product_columns WHERE data->>'product_id' = '00000000-0000-3000-8000-a10000000003';
        
