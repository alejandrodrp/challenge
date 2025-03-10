from typing import List

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, Mapped
from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin
# from app.models.doctor_especialidad import DoctorEspecialidad


class Especialidad(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "especialidad"

    id: Mapped[int] = Column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = Column(String(100), unique=True, nullable=False)
    descripcion: Mapped[str] = Column(String(255), nullable=True)

    doctores: Mapped[List["DoctorEspecialidad"]] = relationship(
        back_populates="especialidad")
