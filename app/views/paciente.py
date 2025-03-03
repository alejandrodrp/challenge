from pydantic import BaseModel
from datetime import date

class PacienteBase(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: date
    direccion: str
    telefono: str
    email: str
    seguro_medico_id: int

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(PacienteBase):
    pass

class PacienteInDBBase(PacienteBase):
    id: int

    class Config:
        from_attributes = True

class Paciente(PacienteInDBBase):
    pass


paciente_schemas = {
    "get": {"input": PacienteBase, "output": PacienteInDBBase},
    "post": {"input": PacienteBase, "output": PacienteInDBBase},
    "put": {"input": PacienteBase, "output": PacienteInDBBase},
    "delete": {"input": PacienteBase, "output": PacienteInDBBase},
}