from typing import List
import uuid, logging
# from schemas.BizIntroducer import BizIntroducerCreate, BizIntroducerResult
from schemas.Profession import ProfessionalGroupCreate, ProfessionalGroupResult, ProfessionCreate, ProfessionResult
from models.Profession import Profession
from models.ProfessionalGroup import ProfessionalGroup
from models.BizIntroducer import BizIntroducer
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class ProfessionalGroupRepo:
    
    q_builder = QueryBuilder(model=None).table("professional_groups")
        
    async def create(e: ProfessionalGroupCreate):
        res = {
            'errors': {},
            'data': None,
        }

        try:
            db_item = ProfessionalGroup()
            db_item.id=str(uuid.uuid4()),
            db_item.name=e.name
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Professional group %s already exists" % e.name)
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res


    async def delete(id: str):
        result = ProfessionalGroup.find(id).delete()

        return result


    def fetch_all() -> List[ProfessionalGroupResult]:
        result =  ProfessionalGroup.all()
        
        return result.serialize()
    
    # def fetch_min() -> List[ProfessionalGroupResult]:
    #     result = ProfessionalGroupRepo.q_builder\
    #         .left_join('titles', 'titles.id', '=', 'agents.title_id')\
    #         .select(
    #             'id', 'titles.name as title', #'email'
    #         )\
    #         .select_raw("first_name ||' '||last_name AS name").get()
        
    #     return result.serialize()


class ProfessionRepo:
    
    q_builder = QueryBuilder(model=Profession).table("professions")
        
    async def create(e: ProfessionCreate):
        res = {
            "errors": {}, "data": None
        }

        try:
            db_item = Profession()
            db_item.id=str(uuid.uuid4())
            db_item.name=e.name
            db_item.group_id=e.group_id
            db_item.code=e.code            
            db_item.save()
            res['data'] = db_item.serialize()
            
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Profession %s already exists" % e.first_name+" | "+e.last_name)
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res


    async def delete(id: str):
        result = Profession.find(id).delete()

        return result


    def fetch_all() -> List[ProfessionResult]:
        result = Profession.with_('group')\
            .order_by("professions.name", "asc")\
            .all()
        
        return result.serialize()


    def fetch_min() -> List[ProfessionResult]:
        result = ProfessionRepo.q_builder\
            .left_join('professional_groups', 'professional_groups.id', '=', 'professions.group_id')\
            .select(
                'professions.id', 'professions.name', 'professional_groups.name as prof_group'
            )\
            .order_by("professions.name", "asc")\
            .get()
        
        return result.serialize()
