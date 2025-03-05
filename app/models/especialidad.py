from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin
from app.models.doctor_especialidad import DoctorEspecialidad


class Especialidad(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "especialidad"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)

    doctores = relationship(
        "DoctorEspecialidad",
        back_populates="especialidad"
    )
