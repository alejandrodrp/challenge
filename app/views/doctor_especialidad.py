from pydantic import BaseModel


class DoctorEspecialidadBase(BaseModel):
    doctor_id: int
    especialidad_id: int


class DoctorEspecialidadCreate(DoctorEspecialidadBase):
    pass


class DoctorEspecialidadUpdate(DoctorEspecialidadBase):
    pass


class DoctorEspecialidadInDBBase(DoctorEspecialidadBase):
    class Config:
        from_attributes = True


class DoctorEspecialidad(DoctorEspecialidadInDBBase):
    pass


doctor_especialidad_schemas = {
    "get": {"input": DoctorEspecialidadBase, "output": DoctorEspecialidadInDBBase},
    "post": {"input": DoctorEspecialidadBase, "output": DoctorEspecialidadInDBBase},
    "put": {"input": DoctorEspecialidadBase, "output": DoctorEspecialidadInDBBase},
    "delete": {"input": DoctorEspecialidadBase, "output": DoctorEspecialidadInDBBase},
}
