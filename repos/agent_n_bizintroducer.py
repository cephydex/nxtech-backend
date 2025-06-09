from typing import List
import uuid, logging
from schemas.BizIntroducer import BizIntroducerCreate, BizIntroducerResult
from schemas.Agent import AgentCreate, AgentResult
from models.Agent import Agent
from models.BizIntroducer import BizIntroducer
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class AgentRepo:
    
    q_builder = QueryBuilder(model=None).table("agents")
        
    async def create(e: AgentCreate):
        res = {
            'errors': {},
            'data': None,
        }

        try:
            db_item = Agent()
            db_item.id=str(uuid.uuid4()),
            db_item.title_id=e.title_id,
            db_item.first_name=e.first_name,
            db_item.last_name=e.last_name,
            db_item.email=e.email,
            db_item.mobile_no=e.mobile_no,
            db_item.address=e.address,
            db_item.company_name=e.company_name,
            # db_item.user_id=e.user_id,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Agent %s already exists" % e.first_name+" | "+e.last_name)
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res


    async def delete(id: str):
        result = Agent.find(id).delete()

        return result


    def fetch_all() -> List[AgentResult]:
        result =  Agent.with_('title').all()
        
        return result.serialize()
    
    def fetch_min() -> List[AgentResult]:
        result = AgentRepo.q_builder\
            .left_join('titles', 'titles.id', '=', 'agents.title_id')\
            .select(
                'id', 'titles.name as title', #'email'
            )\
            .select_raw("first_name ||' '||last_name AS name").get()
        
        return result.serialize()


class BizIntroducerRepo:
    
    q_builder = QueryBuilder(model=BizIntroducer).table("biz_introducers")
        
    async def create(e: BizIntroducerCreate):
        res = {
            "errors": {},
            "data": None
        }

        try:
            db_item = BizIntroducer()
            db_item.id=str(uuid.uuid4())
            db_item.title_id=e.title_id
            db_item.first_name=e.first_name
            db_item.last_name=e.last_name
            db_item.email=e.email
            db_item.mobile_no=e.mobile_no
            db_item.address=e.address
            db_item.company_name=e.company_name
            db_item.location=e.location
            # db_item.user_id=e.user_id
            
            db_item.save()
            res['data'] = db_item.serialize()
            
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("BizIntroducer %s already exists" % e.first_name+" | "+e.last_name)
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res


    async def delete(id: str):
        result = BizIntroducer.find(id).delete()

        return result


    def fetch_all() -> List[BizIntroducerResult]:
        result = BizIntroducer.with_('title').all()
        
        return result.serialize()


    def fetch_min() -> List[BizIntroducerResult]:
        result = BizIntroducer.with_('title').all()
        result = BizIntroducerRepo.q_builder\
            .left_join('titles', 'titles.id', '=', 'biz_introducers.title_id')\
            .select(
                'id', 'titles.name as title', #'email'
            )\
            .select_raw("first_name ||' '||last_name AS name").get()
        # builder.table('users').select('username').get()
        # builder.table('users').left_join('table1', 'table2.id', '=', 'table1.table_id')
        # builder.table('users').right_join('table1', 'table2.id', '=', 'table1.table_id')
        # salary = builder.table('users').sum('salary').first().salary
        # builder.statement("select count(*) from users where active = '?'", [1])
        
        return result.serialize()
