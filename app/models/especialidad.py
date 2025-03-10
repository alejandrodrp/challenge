from typing import List

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin
# from app.models.doctor_especialidad import DoctorEspecialidad


class Especialidad(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "especialidad"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    descripcion: Mapped[str] = mapped_column(String(255), nullable=True)

    doctores: Mapped[List["DoctorEspecialidad"]] = relationship(
        back_populates="especialidad")
