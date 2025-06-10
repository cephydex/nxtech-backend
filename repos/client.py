from typing import List
import uuid, logging
from schemas.Client import ClientCreate, ClientResult
from models.Client import Client
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class ClientRepo:
    
    q_builder = QueryBuilder(model=None).table("agents")
        
    async def create(e: ClientCreate):
        res = {
            'errors': {},
            'data': None,
        }
        
        # title_id, first_name, last_name, other_names
        # , address1, address2, email, mobile_no, mobile_no2, tel_no
        # , dob, company_name, marital_status, active_status, biz_intro_id, professional_group_id, profession_id, nationality_id, 
        # , driver_license_cat, driver_license_no, account_no, national_id (ghana_card)

        try:
            db_item = Client()
            db_item.id=str(uuid.uuid4()),
            db_item.title_id=e.title_id,
            db_item.account_no=e.account_no,
            db_item.first_name=e.first_name,
            db_item.last_name=e.last_name,
            db_item.other_names=e.other_names,
            db_item.email=e.email,
            db_item.mobile_no=e.mobile_no,
            db_item.mobile_no2=e.mobile_no2,
            db_item.address=e.address,
            db_item.address2=e.address2,
            db_item.tel_no=e.tel_no,
            db_item.dob=e.dob,
            db_item.national_id=e.national_id,
            db_item.nationality_id=e.nationality_id,
            db_item.marital_status=e.marital_status,            
            db_item.created_by=e.created_by,
            
            db_item.biz_intro_id=e.biz_intro_id,
            # db_item.agent_id=e.agent_id,
            db_item.professional_group_id=e.professional_group_id,
            db_item.profession_id=e.profession_id,
            db_item.driver_license_cat=e.driver_license_cat,
            db_item.driver_license_no=e.driver_license_no,
            
            db_item.company_name=e.company_name,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Client %s already exists" % e.first_name+" | "+e.last_name)
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res
    
    
    def getLastClientId() -> ClientResult:
        res = Client.order_by("created_at", "desc").limit(1) \
                .get(["id", "account_no", "created_at"]).first()
        all_data = None
        if res:
            all_data = res.serialize()

        return all_data


    async def delete(id: str):
        result = Client.find(id).delete()

        return result


    def fetch_all() -> List[ClientResult]:
        result =  Client.with_('title').all()
        
        return result.serialize()


    def fetch_by_id(id: str) -> List[ClientResult]:
        result =  Client.with_('title')\
                    .with_('nationality')\
                        .with_('profession')\
                            .with_('professional_group')\
                                .with_('biz_introducer')\
                                    .find(id)
        return result.serialize()
    
    
    # def fetch_min() -> List[ClientResult]:
    #     result = AgentRepo.q_builder\
    #         .left_join('titles', 'titles.id', '=', 'agents.title_id')\
    #         .select(
    #             'id', 'titles.name as title', #'email'
    #         )\
    #         .select_raw("first_name ||' '||last_name AS name").get()
        
    #     return result.serialize()

