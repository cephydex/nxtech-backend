from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    active_status: Optional[str] = 'active'
    # blocked_reason: Optional[str] = None
    role_id: str

    created_at: Optional[str] = None
    updated_at: Optional[str] = None


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
