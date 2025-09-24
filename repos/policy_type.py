from typing import List
import uuid, logging
from schemas.PolicyType import PolicyTypeCreate, PolicyTypeResult
from models.PolicyType import PolicyType
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class PolicyTypeRepo:
    
    q_builder = QueryBuilder(model=None).table("policy_types")
        
    async def create(e: PolicyTypeCreate):
        res = {'errors': {}, 'data': None,}

        try:
            db_item = PolicyType()
            db_item.id=str(uuid.uuid4())
            db_item.cat_id=e.cat_id
            db_item.name=e.name
            db_item.description=e.description
            db_item.commission=e.commission
            # db_item.created_by=e.created_by,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Policy type %s already exists" % e.name+" | ("+e.description+", "+e.commission+")")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res

    async def delete(id: str):
        result = PolicyType.find(id).delete()

        return result


    def fetch_all() -> List[PolicyTypeResult]:
        result =  PolicyType.all()
        
        return result.serialize()


    def fetch_all_min() -> List[PolicyTypeResult]:
        result =  PolicyType.all(["id", "name", "commission"])
        
        return result.serialize()


    def fetch_all_with_product() -> List[PolicyTypeResult]:
        result =  PolicyTypeRepo.q_builder\
            .left_join('policy_categories', 'policy_categories.id', '=', 'policy_types.cat_id')\
            .select(
                'id', 'policy_categories.name as category_name', 'policy_types.name', 'policy_types.commission'
            ).all()
        # result =  PolicyType.all(["id", "name", "commission"])
        
        return result.serialize()


    def fetch_by_id(id: str) -> List[PolicyTypeResult]:
        tmp_result =  PolicyType\
                        .with_('policy_category')\
                            .find(id)
        result = tmp_result.serialize() if tmp_result else None
        return result


    def fetch_by_category_id(cat_id: str) -> List[PolicyTypeResult]:
        tmp_result =  PolicyType\
                        .with_('policy_category')\
                            .where('cat_id', cat_id)\
                                .get()
        result = tmp_result.serialize() if tmp_result else None
        return result
