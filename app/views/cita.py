from pydantic import BaseModel
from datetime import date

class CitaBase(BaseModel):
    fecha: date
    hora: str
    motivo: str
    estado: str
    costo: float
    paciente_id: int
    doctor_id: int

class CitaCreate(CitaBase):
    pass

class CitaUpdate(CitaBase):
    pass

class CitaInDBBase(CitaBase):
    id: int

    class Config:
        from_attributes = True

class Cita(CitaInDBBase):
    pass

cita_schemas = {
    "get": {"input": CitaBase, "output": CitaInDBBase},
    "post": {"input": CitaBase, "output": CitaInDBBase},
    "put": {"input": CitaBase, "output": CitaInDBBase},
    "delete": {"input": CitaBase, "output": CitaInDBBase},
}