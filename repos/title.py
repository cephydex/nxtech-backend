from typing import List
from gql.schemas import data_schema
from models.Title import Title
from schemas.Title import  TitleCreate, TitleResult
import logging, uuid

logger = logging.getLogger(__name__)

class TitleRepo:
        
    async def create(title: TitleCreate):
        res = {
            "errors": {},
            "data": None
        }

        try:
            db_item = Title()
            db_item.id=str(uuid.uuid4())
            db_item.name=title.name
            db_item.save()
            res['data'] = db_item.serialize()
            
        except Exception as ex:
            if 'unique constraint' in str(ex):
                logger.error("Title %s already exists" % title.name)
                res['errors']["unique_constraint"] = str(ex)
            logger.error(str(ex))
        
        return res


    async def delete(id: str):
        result = Title.find(id).delete()
        
        return result


    def fetch_all() -> List[TitleResult]:
        result = Title.all()
        
        return result.serialize()