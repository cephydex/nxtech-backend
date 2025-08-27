from typing import List
import uuid
import logging
import traceback
from schemas.Project import ProjectCreate, ProjectCreateMany
from models.Project import Project
from models.ProspectionStage import ProspectionStage
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
            db_item.policy_type_id=e.policy_type_id
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
        
    async def create_multiple(e: ProjectCreateMany):
        res = {'errors': {}, 'data': None,}
        db_data = []
        stg_data = []
        try:
            for project in e.projects:
                u_id = str(uuid.uuid4())
                db_data.append({
                    "id": u_id,
                    "prospect_id": e.prospect_id,
                    "policy_type_id": project.policy_type_id,
                    "status": project.stage,
                    "created_by": e.created_by,
                })

                stg_data.append({
                    "project_id": u_id,
                    "stage": project.stage,
                    "notes": project.stage,
                    "created_by": e.created_by,
                })

            pj_result = Project.bulk_create(db_data)
            stg_res = ProspectionStage.bulk_create(stg_data)
            res['data'] = pj_result.serialize()
            res['stages'] = stg_res.serialize()

        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Multiple project detail already exists")
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

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


    def fetch_all_gen_by_prospect(prospect_id: str) -> List:
        result =  ProjectRepo.q_builder\
            .left_join('prospects', 'prospects.id', '=', 'projects.prospect_id')\
            .select(
                'id', 'prospects.client_type', 'prospects.first_name', 'prospects.last_name', 
                'prospects.email', 'prospects.company_name', "prospects.source", "created_at", "prospect_id"
            )\
                .where('prospect_id', prospect_id)\
            .get()
        
        return result.serialize()


    def fetch_by_id(id: str) -> List:
        tmp_result =  Project\
                    .with_('prospect')\
                        .with_('stages')\
                            .find(id)
        result = tmp_result.serialize() if tmp_result else None
        return result


    def fetch_by_prospect_id(id: str) -> List:
        tmp_result =  Project\
                    .with_('prospect')\
                        .with_('stages')\
                            .where('prospect_id', id)\
                                .get()
        result = tmp_result.serialize() if tmp_result else None
        return result
