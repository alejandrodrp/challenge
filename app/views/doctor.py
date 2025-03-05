from pydantic import BaseModel


class DoctorBase(BaseModel):
    nombre: str
    apellido: str
    telefono: str
    email: str
    licencia_medica: str
    activo: bool


class DoctorCreate(DoctorBase):
    pass


class DoctorUpdate(DoctorBase):
    pass


class DoctorInDBBase(DoctorBase):
    id: int

    class Config:
        from_attributes = True


class Doctor(DoctorInDBBase):
    pass


doctor_schemas = {
    "get": {"input": DoctorBase, "output": DoctorInDBBase},
    "post": {"input": DoctorBase, "output": DoctorInDBBase},
    "put": {"input": DoctorBase, "output": DoctorInDBBase},
    "delete": {"input": DoctorBase, "output": DoctorInDBBase},
}
