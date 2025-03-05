from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class Cita(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "cita"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    hora = Column(String(10), nullable=False)  
    motivo = Column(String(255), nullable=False)
    estado = Column(String(50), default="pendiente")  # pendiente, completada, cancelada
    costo = Column(Float, nullable=False)
    paciente_id = Column(Integer, ForeignKey('paciente.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=False)

    paciente = relationship("Paciente", back_populates="citas")
    doctor = relationship("Doctor", back_populates="citas")