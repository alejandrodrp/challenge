from typing import Annotated

from pydantic import BaseModel, EmailStr, ConfigDict, BeforeValidator

from app.views.types.output_input_schemas import OperationSchemaType
from app.views.validators.password import validate_password


class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(BaseModel):
    password: Annotated[str, BeforeValidator(validate_password)]
    username: str
    email: EmailStr
    is_active: bool = True


class UserUpdate(UserCreate):
    pass


class UserInDBBase(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UserPublic(UserBase):
    pass


user_schemas: OperationSchemaType = {
    "get": {"input": UserBase, "output": UserInDBBase},
    "post": {"input": UserCreate, "output": UserInDBBase},
    "put": {"input": UserUpdate, "output": UserInDBBase},
    "delete": {"input": UserBase, "output": UserInDBBase},
}
