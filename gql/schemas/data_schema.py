from pydantic import BaseModel, ConfigDict
import strawberry


@strawberry.type
class Title(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(from_attributes=True)
    # class Config:
    #     orm_mode = True


@strawberry.input
class TitleInput:
    # id: str
    name: str
