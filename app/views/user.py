from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(BaseModel):
    password: str
    username: str
    email: EmailStr
    is_active: bool = True


class UserUpdate(UserCreate):
    pass


class UserInDBBase(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserPublic(UserBase):
    pass


user_schemas = {
    "get": {"input": UserBase, "output": UserInDBBase},
    "post": {"input": UserCreate, "output": UserInDBBase},
    "put": {"input": UserUpdate, "output": UserInDBBase},
    "delete": {"input": UserBase, "output": UserInDBBase},
}
