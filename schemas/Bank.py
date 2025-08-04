from pydantic import BaseModel, ConfigDict
# from typing import Optional


class BankBase(BaseModel):
    name: str
    code: str


class BankCreate(BankBase):
    pass


class BankResult(BankBase):
    id:str

    model_config = ConfigDict(from_attributes=True)

