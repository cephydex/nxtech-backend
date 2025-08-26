from typing import List
import uuid, logging
from schemas.PolicyCategory import PolicyCategoryCreate, PolicyCategoryResult
from models.PolicyCategory import PolicyCategory
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class PolicyCategoryRepo:
    
    q_builder = QueryBuilder(model=None).table("policy_categories")
        
    async def create(e: PolicyCategoryCreate):
        res = {'errors': {}, 'data': None,}

        try:
            db_item = PolicyCategory()
            db_item.id=str(uuid.uuid4())
            db_item.name=e.name
            db_item.description=e.description
            # db_item.created_by=e.created_by,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Policy category %s already exists" % e.name+" | ("+e.description+", "+e.commission+")")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res

    async def delete(id: str):
        result = PolicyCategory.find(id).delete()

        return result


    def fetch_all() -> List[PolicyCategoryResult]:
        result =  PolicyCategory.all()
        
        return result.serialize()


    def fetch_all_min() -> List[PolicyCategoryResult]:
        result =  PolicyCategory.all(["id", "name"])
        
        return result.serialize()


    def fetch_by_id(id: str) -> List[PolicyCategoryResult]:
        tmp_result =  PolicyCategory .find(id)
        result = tmp_result.serialize() if tmp_result else None
        return result
