from fastapi import APIRouter
from app.controllers.base_controller import BaseController

# Schemas
from app.views.cita import cita_schemas
from app.views.paciente import paciente_schemas
from app.views.tratamiento import tratamiento_schemas
from app.views.seguro_medico import seguro_medico_schemas
from app.views.historial_medico import historial_medico_schemas
from app.views.doctor import doctor_schemas
from app.views.especialidad import especialidad_schemas
from app.views.doctor_especialidad import doctor_especialidad_schemas

# Models
from app.models.cita import Cita
from app.models.paciente import Paciente
from app.models.tratamiento import Tratamiento
from app.models.seguro_medico import SeguroMedico
from app.models.historial_medico import HistorialMedico
from app.models.doctor import Doctor
from app.models.especialidad import Especialidad
from app.models.doctor_especialidad import doctor_especialidad

central_router = APIRouter()

# Incluir routers para cada modelo
central_router.include_router(
    BaseController(model=Cita, schemas=cita_schemas).router, prefix="/cita", tags=["Cita"]
)
central_router.include_router(
    BaseController(model=Paciente, schemas=paciente_schemas).router, prefix="/paciente", tags=["Paciente"]
)
central_router.include_router(
    BaseController(model=Tratamiento, schemas=tratamiento_schemas).router, prefix="/tratamiento", tags=["Tratamiento"]
)
central_router.include_router(
    BaseController(model=SeguroMedico, schemas=seguro_medico_schemas).router, prefix="/seguro_medico", tags=["SeguroMedico"]
)
central_router.include_router(
    BaseController(model=HistorialMedico, schemas=historial_medico_schemas).router, prefix="/historial_medico", tags=["HistorialMedico"]
)
central_router.include_router(
    BaseController(model=Doctor, schemas=doctor_schemas).router, prefix="/doctor", tags=["Doctor"]
)
central_router.include_router(
    BaseController(model=Especialidad, schemas=especialidad_schemas).router, prefix="/especialidad", tags=["Especialidad"]
)
central_router.include_router(
    BaseController(model=Doctor, schemas=doctor_especialidad_schemas).router, prefix='/doctor_especialidad', tags=["Doctor", "Especialidad"]
)
