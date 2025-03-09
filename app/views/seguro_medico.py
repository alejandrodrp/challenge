from pydantic import BaseModel, ConfigDict
from app.views.types.output_input_schemas import OperationSchemaType


class SeguroMedicoBase(BaseModel):
    nombre: str
    cobertura: str
    contacto: str


class SeguroMedicoCreate(SeguroMedicoBase):
    pass


class SeguroMedicoUpdate(SeguroMedicoBase):
    pass


class SeguroMedicoInDBBase(SeguroMedicoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SeguroMedico(SeguroMedicoInDBBase):
    pass


seguro_medico_schemas: OperationSchemaType = {
    "get": {"input": SeguroMedicoBase, "output": SeguroMedicoInDBBase},
    "post": {"input": SeguroMedicoBase, "output": SeguroMedicoInDBBase},
    "put": {"input": SeguroMedicoBase, "output": SeguroMedicoInDBBase},
    "delete": {"input": SeguroMedicoBase, "output": SeguroMedicoInDBBase},
}
