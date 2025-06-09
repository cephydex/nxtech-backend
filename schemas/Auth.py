from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class RoleBase(BaseModel):
    name:str
    description:Optional[str] = None


class RoleCreate(RoleBase):
    pass


class RoleResult(RoleBase):
    id:str

    model_config = ConfigDict(from_attributes=True)


class AdminMinBase(BaseModel):
    first_name: str
    last_name: str
    other_names: Optional[str] = None
    sex: str
    email: Optional[str] = None
    phone: str
    password: str
    active_status:str = 'active'
    inst: str


class AdminBase(BaseModel):
    first_name: str
    last_name: str
    other_names: Optional[str] = None
    sex: str
    email: Optional[str] = None
    phone: str
    password: str
    active_status: Optional[str] = 'active'
    blocked_reason: Optional[str] = None
    role_id: str
    inst: str

    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class AdminCreate(AdminBase):
    role_id: str
    pass


class AdminUserCreate(AdminMinBase):
    pass


class AdminResult(AdminBase):
    id:str

    # class Config:
    #     from_attributes=True
    #     populate_by_name = True

    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    email:str
    password:str


class AdminUpdateProfile(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    other_names: Optional[str] = None
    phone: Optional[str] = None


class AdminChangePassword(BaseModel):
    current_password:str = Field(...,min_length=5)
    password:str = Field(...,min_length=5)
    password_confirmation:str


class InstBase(BaseModel):
    name:str
    description: Optional[str] = None
    address: Optional[str] = None
    phone_no:str
    email: Optional[str] = None


class InstCreate(InstBase):
    pass


class InstResult(InstBase):
    id:str

    model_config = ConfigDict(from_attributes=True)