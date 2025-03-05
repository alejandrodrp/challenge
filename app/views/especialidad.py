from pydantic import BaseModel

class EspecialidadBase(BaseModel):
    nombre: str
    descripcion: str

class EspecialidadCreate(EspecialidadBase):
    pass

class EspecialidadUpdate(EspecialidadBase):
    pass

class EspecialidadInDBBase(EspecialidadBase):
    id: int

    class Config:
        from_attributes = True

class Especialidad(EspecialidadInDBBase):
    pass


especialidad_schemas = {
    "get": {"input": EspecialidadBase, "output": EspecialidadInDBBase},
    "post": {"input": EspecialidadBase, "output": EspecialidadInDBBase},
    "put": {"input": EspecialidadBase, "output": EspecialidadInDBBase},
    "delete": {"input": EspecialidadBase, "output": EspecialidadInDBBase},
}