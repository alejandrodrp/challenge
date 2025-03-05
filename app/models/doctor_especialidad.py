from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.mixins import TimestampMixin, SoftDeleteMixin


class DoctorEspecialidad(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = 'doctor_especialidad'
    id = Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = Column(Integer, ForeignKey('doctor.id'), primary_key=True)
    especialidad_id = Column(Integer, ForeignKey('especialidad.id'), primary_key=True)

    doctor = relationship("Doctor", back_populates="especialidades")
    especialidad = relationship("Especialidad", back_populates="doctores")
