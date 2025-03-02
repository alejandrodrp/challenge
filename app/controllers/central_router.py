from fastapi import APIRouter
from app.controllers.base_controller import BaseController
from app.models.cita import Cita


central_router = APIRouter()

central_router.include_router(
    BaseController().router, prefix="/cita", tags=["Cita"])
