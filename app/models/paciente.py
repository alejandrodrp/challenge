from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class Paciente(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "paciente"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    direccion = Column(String(255), nullable=True)
    telefono = Column(String(20), nullable=True)
    email = Column(String(100), unique=True, nullable=True)
    seguro_medico_id = Column(Integer, ForeignKey('seguro_medico.id'), nullable=True)

    seguro_medico = relationship("SeguroMedico", back_populates="pacientes")
    citas = relationship("Cita", back_populates="paciente")
    historial_medico = relationship("HistorialMedico", back_populates="paciente", uselist=False)