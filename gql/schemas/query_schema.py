import strawberry
from pydantic import typing
from strawberry.types import Info
from gql.controllers import Queries
from typing import List
from models_old.title_model import Title
from gql.schemas import data_schema as schemas
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)


@strawberry.type
class Query:

    get_all_titles:List[schemas.Title] = strawberry.field(resolver=Queries.get_all_titles)

    # @strawberry.field
    # def get_all_title(self, info:strawberry.Info) -> List[schemas.Title]:
    #     db:Session = info.context["db"]
    #     logger.warning("DB SESSION")
    #     logger.warning(db)
    #     titles = Queries.get_all_titles(self, db)
    #     # if not len(titles):
    #     #     raise Exception(status_code=400, content= "Can't find resources")
        
    #     return titles
        

    @strawberry.field
    def hello(self) -> str:
        return "Hello masonite"