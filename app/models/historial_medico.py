from datetime import datetime
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin

class HistorialMedico(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "historial_medico"

    id = Column(Integer, primary_key=True, autoincrement=True)
    diagnostico = Column(String(255), nullable=False)
    tratamiento = Column(String(255), nullable=True)
    fecha_registro = Column(Date, default=datetime.now())
    paciente_id = Column(Integer, ForeignKey('paciente.id'), nullable=False)

    paciente = relationship("Paciente", back_populates="historial_medico")
    tratamientos = relationship("Tratamiento", back_populates="historial_medico")