from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class TitleBase(BaseModel):
    name: str


class TitleCreate(TitleBase):
    pass


class TitleResult(TitleBase):
    id:str

    model_config = ConfigDict(from_attributes=True)

