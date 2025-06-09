# from sqlalchemy.orm import Session
from utils.lib import get_db
# from models.title_model import Title
from .schemas import data_schema
from models_old import title_model
import strawberry
import logging
from typing import List

logger = logging.getLogger(__name__)
from repos.title import TitleRepo

class Queries:

    # def get_all_titles(self, db:Session)-> List[data_schema.Title]:
    
    def get_all_titles(self, info:strawberry.Info)-> List[data_schema.Title]:
        db:Session = info.context["db"]
        # result = db.query(title_model.Title).all()
        return TitleRepo.fetch_all(db)



class Mutations:

    def add_title(self, info:strawberry.Info, input:data_schema.TitleInput)-> data_schema.Title:
        db:Session = info.context["db"]
        return TitleRepo.create(db, input)
        