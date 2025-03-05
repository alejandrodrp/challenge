from pydantic import BaseModel
from datetime import date

class HistorialMedicoBase(BaseModel):
    diagnostico: str
    tratamiento: str
    fecha_registro: date
    paciente_id: int

class HistorialMedicoCreate(HistorialMedicoBase):
    pass

class HistorialMedicoUpdate(HistorialMedicoBase):
    pass

class HistorialMedicoInDBBase(HistorialMedicoBase):
    id: int

    class Config:
        from_attributes = True

class HistorialMedico(HistorialMedicoInDBBase):
    pass


historial_medico_schemas = {
    "get": {"input": HistorialMedicoBase, "output": HistorialMedicoInDBBase},
    "post": {"input": HistorialMedicoBase, "output": HistorialMedicoInDBBase},
    "put": {"input": HistorialMedicoBase, "output": HistorialMedicoInDBBase},
    "delete": {"input": HistorialMedicoBase, "output": HistorialMedicoInDBBase},
}