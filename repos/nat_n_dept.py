from typing import List
import uuid, logging
from schemas.Nationality import NationalityCreate, NationalityResult
from schemas.Department import DepartmentCreate, DepartmentResult
from models.Nationality import Nationality
from models.Department import Department

logger = logging.getLogger(__name__)

class NationalityRepo:
        
    # async def create(nat: NationalityCreate):
    #     res = {
    #         'errors': {},
    #         'data': None,
    #     }
    #     try:
    #         db_item = Nationality()
    #         db_item.id=str(uuid.uuid4()),
    #         db_item.num_code=nat.num_code,
    #         db_item.alpha_2_code=nat.alpha_2_code,
    #         db_item.alpha_3_code=nat.alpha_3_code,
    #         db_item.short_name=nat.short_name,
    #         db_item.nationality=nat.nationality,
    #         db_item.save()
    #         res['data'] = db_item.serialize()

    #     except Exception as ex:
    #         if 'unique constraint' in str(ex):
    #             logger.error("Nationality %s already exists" % nat.short_name+" | "+nat.nationality)
    #             res['errors']["unique_constraint"] = str(ex)
    #         logger.error(str(ex))

    #     return res
        


    # async def delete(db:Session, id: str):
    #     result = Nationality.find(id).delete()

    #     return result


    def fetch_all() -> List[NationalityResult]:
        result =  Nationality.all()
        
        return result.serialize()


class DepartmentRepo:
        
    async def create(d: DepartmentCreate):
        res = {
            "errors": {},
            "data": None
        }

        try:
            db_item = Department()
            db_item.id=str(uuid.uuid4()),
            db_item.name=d.name,
            db_item.code=d.code,
            db_item.description=d.description,
            
            db_item.save()
            res['data'] = db_item.serialize()
            
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Department %s already exists" % d.name+" | "+d.description)
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))

        return res


    # async def delete(id: str):
    #     result = Department.find(id).delete()

    #     return result


    def fetch_all() -> List[DepartmentResult]:
        #  res = MusigaProject.with_("project_type").all()
        result = Department.all()
        
        return result.serialize()