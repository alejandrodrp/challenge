from pydantic import BaseModel, ConfigDict
from app.views.types.output_input_schemas import OperationSchemaType


class TratamientoBase(BaseModel):
    nombre: str
    descripcion: str
    costo_estimado: float
    duracion_dias: int
    historial_medico_id: int


class TratamientoCreate(TratamientoBase):
    pass


class TratamientoUpdate(TratamientoBase):
    pass


class TratamientoInDBBase(TratamientoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class Tratamiento(TratamientoInDBBase):
    pass


tratamiento_schemas: OperationSchemaType = {
    "get": {"input": TratamientoBase, "output": TratamientoInDBBase},
    "post": {"input": TratamientoBase, "output": TratamientoInDBBase},
    "put": {"input": TratamientoBase, "output": TratamientoInDBBase},
    "delete": {"input": TratamientoBase, "output": TratamientoInDBBase},
}
