from pydantic import BaseModel, ConfigDict
from app.views.types.output_input_schemas import OperationSchemaType


class DoctorEspecialidadBase(BaseModel):
    doctor_id: int
    especialidad_id: int


class DoctorEspecialidadCreate(DoctorEspecialidadBase):
    pass


class DoctorEspecialidadUpdate(DoctorEspecialidadBase):
    pass


class DoctorEspecialidadInDBBase(DoctorEspecialidadBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class DoctorEspecialidad(DoctorEspecialidadInDBBase):
    pass


doctor_especialidad_schemas: OperationSchemaType = {
    "get": {"input": DoctorEspecialidadBase, "output": DoctorEspecialidadInDBBase},
    "post": {"input": DoctorEspecialidadBase, "output": DoctorEspecialidadInDBBase},
    "put": {"input": DoctorEspecialidadBase, "output": DoctorEspecialidadInDBBase},
    "delete": {"input": DoctorEspecialidadBase, "output": DoctorEspecialidadInDBBase},
}
