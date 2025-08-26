from typing import List
import uuid
import logging
import traceback
from schemas.Project import ProjectCreate
from models.Project import Project
from masoniteorm.query import QueryBuilder

logger = logging.getLogger(__name__)

class ProjectRepo:
    
    q_builder = QueryBuilder(model=None).table("projects")
        
    async def create(e: ProjectCreate):
        res = {'errors': {}, 'data': None,}

        try:
            db_item = Project()
            db_item.id=str(uuid.uuid4())
            db_item.prospect_id=e.prospect_id
            # if e.policy_type_id is not None:
            #     db_item.policy_type_id=e.policy_type_id
            db_item.status=e.status
            db_item.created_by=e.created_by,
            db_item.save()
            res['data'] = db_item.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error(f"Project %s already exists {e.prospect_id} | ({e.status})")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))
            # print(traceback.format_exc())
            # traceback.print_exc()

        return res
        
    async def update(id:str, e: ProjectCreate):
        res = {'errors': {}, 'data': None,}

        try:
            upd_data = {}
            db_item = Project.find(id)

            if e.policy_type_id is not None:
                upd_data.update({"policy_type_id":e.policy_type_id})
            if e.status is not None:
                upd_data.update({"status":e.status})

            db_item.update(upd_data)
            res['data'] = db_item.serialize()

        except Exception as ex:
            res['errors']= str(ex)
            logger.error(str(ex))

        return res

    async def delete(id: str):
        result = Project.find(id).delete()

        return result


    def fetch_all() -> List:
        result =  Project\
                    .with_('prospect')\
                        .with_('stages').all()
        
        return result.serialize()


    def fetch_all_gen() -> List:
        result =  ProjectRepo.q_builder\
            .left_join('prospects', 'prospects.id', '=', 'projects.prospect_id')\
            .select(
                'id', 'prospects.client_type', 'prospects.first_name', 'prospects.last_name', 
                'prospects.email', 'prospects.company_name', "prospects.source", "created_at", "prospect_id"
            )\
            .get()
        
        return result.serialize()


    def fetch_by_id(id: str) -> List:
        tmp_result =  Project\
                    .with_('prospect')\
                        .with_('stages')\
                            .find(id)
        result = tmp_result.serialize() if tmp_result else None
        return result
