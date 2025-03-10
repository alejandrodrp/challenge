from pydantic import BaseModel, ConfigDict
from datetime import date
from app.views.types.output_input_schemas import OperationSchemaType


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

    model_config = ConfigDict(from_attributes=True)


class HistorialMedico(HistorialMedicoInDBBase):
    pass


historial_medico_schemas: OperationSchemaType = {
    "get": {"input": HistorialMedicoBase, "output": HistorialMedicoInDBBase},
    "post": {"input": HistorialMedicoBase, "output": HistorialMedicoInDBBase},
    "put": {"input": HistorialMedicoBase, "output": HistorialMedicoInDBBase},
    "delete": {"input": HistorialMedicoBase, "output": HistorialMedicoInDBBase},
}
