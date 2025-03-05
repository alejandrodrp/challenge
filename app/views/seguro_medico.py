from pydantic import BaseModel


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

    class Config:
        from_attributes = True


class SeguroMedico(SeguroMedicoInDBBase):
    pass


seguro_medico_schemas = {
    "get": {"input": SeguroMedicoBase, "output": SeguroMedicoInDBBase},
    "post": {"input": SeguroMedicoBase, "output": SeguroMedicoInDBBase},
    "put": {"input": SeguroMedicoBase, "output": SeguroMedicoInDBBase},
    "delete": {"input": SeguroMedicoBase, "output": SeguroMedicoInDBBase},
}
