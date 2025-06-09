from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class NationalityBase(BaseModel):
    num_code: str
    alpha_2_code: str
    alpha_3_code: str
    short_name: str
    nationality: str


class NationalityCreate(NationalityBase):
    pass


class NationalityResult(NationalityBase):
    id:str

    model_config = ConfigDict(from_attributes=True)

