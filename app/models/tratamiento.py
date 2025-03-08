from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from app.core.database import Base
# from app.models import HistorialMedico
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class Tratamiento(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "tratamiento"

    id: Mapped[int] = Column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = Column(String(100), nullable=False)
    descripcion: Mapped[str] = Column(String(255), nullable=True)
    costo_estimado: Mapped[float] = Column(nullable=True)
    duracion_dias: Mapped[int] = Column(nullable=True)
    historial_medico_id: Mapped[int] = Column(ForeignKey('historial_medico.id'), nullable=False)

    historial_medico: Mapped["HistorialMedico"] = relationship(back_populates="tratamientos")
