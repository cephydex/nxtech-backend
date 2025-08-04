from typing import List
import uuid, logging
from schemas.Client import ClientCreate, ClientResult, ClientContactCreate, ClientContactResult
from models.Client import Client
from models.ClientContact import ClientContact
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class ClientRepo:
    
    q_builder = QueryBuilder(model=None).table("clients")
        
    async def create(e: ClientCreate):
        res = {'errors': {}, 'data': None,}
        
        # client_type, company_name, address_loc, email, contact_no, is_existing, client_code, company_reg_no, year_of_inc, 
        # uploaded_doc, tin_no, active_status, notes, 
        # account_manager, claims_manager, created_by,
        # title_id, first_name, last_name, other_names, dob, sex, nationality_id, id_type, id_number, pep, 
        # residential_addr, postal_addr, professional_group_id, profession_id,

        try:
            db_item = Client()
            db_item.id=str(uuid.uuid4()),
            db_item.title_id=e.title_id,
            db_item.client_code=e.client_code,
            db_item.first_name=e.first_name,
            db_item.last_name=e.last_name,
            db_item.other_names=e.other_names,
            db_item.email=e.email,
            db_item.contact_no=e.contact_no,
            db_item.dob=e.dob,
            db_item.sex=e.sex,
            db_item.residential_addr=e.residential_addr,
            db_item.postal_addr=e.postal_addr,
            db_item.address_loc=e.address_loc,
            db_item.nationality_id=e.nationality_id,
            db_item.profession_id=e.profession_id,
            db_item.pep=e.pep,
            db_item.client_type=e.client_type,
            db_item.is_existing=e.is_existing,
            db_item.id_type=e.id_type,
            db_item.id_number=e.id_number,
            db_item.tin_no=e.tin_no,

            db_item.company_name=e.company_name,
            db_item.company_reg_no=e.company_reg_no,
            db_item.year_of_inc=e.year_of_inc,
            db_item.professional_group_id=e.professional_group_id,
            db_item.uploaded_doc=e.uploaded_doc,
            db_item.account_manager=e.account_manager,
            db_item.claims_manager=e.claims_manager,
            db_item.active_status=e.active_status,
            db_item.created_by=e.created_by,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Client %s already exists" % e.client_code+" | "+e.client_type+" | ("+e.first_name+", "+e.last_name+")")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res
    
        # client_type, company_name, address_loc, email, contact_no, is_existing, client_code, company_reg_no, year_of_inc, 
        # uploaded_doc, tin_no, active_status, notes, 
        # account_manager, claims_manager, created_by,
        # title_id, first_name, last_name, other_names, dob, sex, nationality_id, id_type, id_number, pep, 
        # residential_addr, postal_addr, professional_group_id, profession_id,
    
    
    def getLastClientId() -> ClientResult:
        res = Client.order_by("created_at", "desc").limit(1) \
                .get(["id", "client_code", "created_at"]).first()
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
        tmp_result =  Client.with_('title')\
                    .with_('nationality')\
                        .with_('profession')\
                            .with_('professional_group')\
                                    .find(id)
        result = tmp_result.serialize() if tmp_result else None
        return result


class ClientContactRepo:
    
    q_builder = QueryBuilder(model=None).table("client_contacts")
        
    async def create(e: ClientContactCreate):
        res = {'errors': {}, 'data': None,}

        try:
            db_item = ClientContact()
            db_item.id=str(uuid.uuid4()),
            db_item.client_id=e.client_id,
            db_item.full_name=e.full_name,
            db_item.contact_no=e.contact_no,
            db_item.email=e.email,
            db_item.role=e.role,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Client contact %s already exists" % e.client_id+" | "+e.full_name+" | ("+e.contact_no+", "+e.role+")")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res
    
        # client_type, company_name, address_loc, email, contact_no, is_existing, client_code, company_reg_no, year_of_inc, 
        # uploaded_doc, tin_no, active_status, notes, 
        # account_manager, claims_manager, created_by,
        # title_id, first_name, last_name, other_names, dob, sex, nationality_id, id_type, id_number, pep, 
        # residential_addr, postal_addr, professional_group_id, profession_id,


    async def delete(id: str):
        result = ClientContact.find(id).delete()

        return result


    def fetch_all() -> List[ClientContactResult]:
        result =  ClientContact.with_('client').all()
        
        return result.serialize()


    def fetch_by_id(id: str) -> List[ClientContactResult]:
        result =  ClientContact.with_('client').find(id)

        return result.serialize()


    def fetch_by_client_id(client_id: str) -> List[ClientContactResult]:
        result =  ClientContact.where('client_id', client_id).get()

        return result.serialize()
    
    
    # def fetch_min() -> List[ClientResult]:
    #     result = AgentRepo.q_builder\
    #         .left_join('titles', 'titles.id', '=', 'agents.title_id')\
    #         .select(
    #             'id', 'titles.name as title', #'email'
    #         )\
    #         .select_raw("first_name ||' '||last_name AS name").get()
        
    #     return result.serialize()

