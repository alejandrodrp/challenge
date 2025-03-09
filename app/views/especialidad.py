from pydantic import BaseModel, ConfigDict
from app.views.types.output_input_schemas import OperationSchemaType


class EspecialidadBase(BaseModel):
    nombre: str
    descripcion: str


class EspecialidadCreate(EspecialidadBase):
    pass


class EspecialidadUpdate(EspecialidadBase):
    pass


class EspecialidadInDBBase(EspecialidadBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Especialidad(EspecialidadInDBBase):
    pass


especialidad_schemas: OperationSchemaType = {
    "get": {"input": EspecialidadBase, "output": EspecialidadInDBBase},
    "post": {"input": EspecialidadBase, "output": EspecialidadInDBBase},
    "put": {"input": EspecialidadBase, "output": EspecialidadInDBBase},
    "delete": {"input": EspecialidadBase, "output": EspecialidadInDBBase},
}
