from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class UserLoginCreate(BaseModel):
    email: str
    username: Optional[str] = None
    password: Optional[str] = None
    active_status: Optional[str] = 'active'
    role_id: str

class UserBase(UserLoginCreate):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    initials: Optional[str] = None
    dept_id: Optional[str] = None
    supervisor_id: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserResult(UserBase):
    id:str
    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    email:str
    password:str


class UserUpdateProfile(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None


class UserChangePassword(BaseModel):
    current_password:str = Field(...,min_length=5)
    password:str = Field(...,min_length=5)
    password_confirmation:str
