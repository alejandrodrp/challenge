from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str

class UserInDBBase(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserPublic(UserBase):
    pass

user_schemas = {
    "get": {"input": UserBase, "output": UserInDBBase},
    "post": {"input": UserBase, "output": UserInDBBase},
    "put": {"input": UserBase, "output": UserInDBBase},
    "delete": {"input": UserBase, "output": UserInDBBase},
}