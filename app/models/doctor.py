from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin
from app.models.doctor_especialidad import doctor_especialidad


class Doctor(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=True)
    email = Column(String(100), unique=True, nullable=True)
    licencia_medica = Column(String(50), unique=True, nullable=False)
    activo = Column(Boolean, default=True)

    especialidades = relationship(
        "Especialidad",
        secondary=doctor_especialidad,
        back_populates="doctores"
    )
