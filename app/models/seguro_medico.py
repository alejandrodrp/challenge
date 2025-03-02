from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class SeguroMedico(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "seguro_medico"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)
    cobertura = Column(String(255), nullable=True)
    contacto = Column(String(100), nullable=True)

    pacientes = relationship("Paciente", back_populates="seguro_medico")