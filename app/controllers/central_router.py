from fastapi import APIRouter
from app.controllers.base_controller import BaseController
from app.models.cita import Cita


# Crear el router central
central_router = APIRouter()

# Incluir el router del controlador base
central_router.include_router(
    BaseController().router, prefix="/cita", tags=["Cita"])
