from typing import List
import uuid, logging
from schemas.BizIntroducer import BizIntroducerCreate, BizIntroducerResult
from schemas.Agent import AgentCreate, AgentResult
from models.Agent import Agent
from models.BizIntroducer import BizIntroducer
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)


class BizIntroducerRepo:
    
    q_builder = QueryBuilder(model=BizIntroducer).table("biz_introducers")
        
    async def create(e: BizIntroducerCreate):
        res = {"errors": {}, "data": None}

        try:
            # title_id, full_name, primary_contact, email, contact_no, address, location, id_type, id_number, business_name, business_reg_no, tin_no
            # , bank_id, bank_account_name, bank_branch_name, bank_account_no, commission_rate, biz_agreement_doc, user_id, itype,
            db_item = BizIntroducer()
            db_item.id=str(uuid.uuid4())
            db_item.title_id=e.title_id
            db_item.full_name=e.full_name
            db_item.primary_contact=e.primary_contact
            db_item.commission_rate=e.commission_rate
            db_item.email=e.email
            db_item.contact_no=e.contact_no
            db_item.address=e.address
            db_item.location=e.location
            db_item.business_name=e.business_name
            db_item.business_reg_no=e.business_reg_no
            db_item.id_type=e.id_type
            db_item.id_number=e.id_number
            db_item.tin_no=e.tin_no

            db_item.bank_id=e.bank_id
            db_item.bank_account_name=e.bank_account_name
            db_item.bank_branch_name=e.bank_branch_name
            db_item.bank_account_no=e.bank_account_no
            db_item.notes=e.notes
            db_item.biz_agreement_doc=e.biz_agreement_doc
            db_item.itype=e.itype
            db_item.user_id=e.user_id
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
            .select_raw("full_name").get()
        # builder.table('users').select('username').get()
        # builder.table('users').left_join('table1', 'table2.id', '=', 'table1.table_id')
        # builder.table('users').right_join('table1', 'table2.id', '=', 'table1.table_id')
        # salary = builder.table('users').sum('salary').first().salary
        # builder.statement("select count(*) from users where active = '?'", [1])
        
        return result.serialize()
