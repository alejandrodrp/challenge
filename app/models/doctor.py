from typing import List

from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship, Mapped,  mapped_column

from app.core.database import Base
from app.models import Cita
from app.models.mixins import SoftDeleteMixin, TimestampMixin
# from app.models.doctor_especialidad import DoctorEspecialidad


class Doctor(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "doctor"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    apellido: Mapped[str] = mapped_column(String(100), nullable=False)
    telefono: Mapped[str] = mapped_column(String(20), nullable=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    licencia_medica = mapped_column(String(50), unique=True, nullable=False)
    activo: Mapped[bool] = mapped_column(default=True)

    especialidades: Mapped[List["DoctorEspecialidad"]] = relationship(
        back_populates="doctor")

    citas: Mapped[List["Cita"]] = relationship(
        back_populates="doctor")
