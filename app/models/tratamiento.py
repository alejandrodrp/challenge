from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class Tratamiento(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "tratamiento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    costo_estimado = Column(Float, nullable=True)
    duracion_dias = Column(Integer, nullable=True)
    historial_medico_id = Column(Integer, ForeignKey('historial_medico.id'), nullable=False)

    historial_medico = relationship("HistorialMedico", back_populates="tratamientos")
