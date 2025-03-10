from pydantic import BaseModel, ConfigDict
from datetime import date
from app.views.types.output_input_schemas import OperationSchemaType


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

    model_config = ConfigDict(from_attributes=True)


class Cita(CitaInDBBase):
    pass


cita_schemas: OperationSchemaType = {
    "get": {"input": CitaBase, "output": CitaInDBBase},
    "post": {"input": CitaBase, "output": CitaInDBBase},
    "put": {"input": CitaBase, "output": CitaInDBBase},
    "delete": {"input": CitaBase, "output": CitaInDBBase},
}
