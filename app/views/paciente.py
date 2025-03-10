from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import date
from app.views.types.output_input_schemas import OperationSchemaType


class PacienteBase(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: date
    direccion: str
    telefono: str
    email: EmailStr
    seguro_medico_id: int


class PacienteCreate(PacienteBase):
    pass


class PacienteUpdate(PacienteBase):
    pass


class PacienteInDBBase(PacienteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Paciente(PacienteInDBBase):
    pass


paciente_schemas: OperationSchemaType = {
    "get": {"input": PacienteBase, "output": PacienteInDBBase},
    "post": {"input": PacienteBase, "output": PacienteInDBBase},
    "put": {"input": PacienteBase, "output": PacienteInDBBase},
    "delete": {"input": PacienteBase, "output": PacienteInDBBase},
}
