from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.database import Base
# from app.models import HistorialMedico
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class Tratamiento(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "tratamiento"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    descripcion: Mapped[str] = mapped_column(String(255), nullable=True)
    costo_estimado: Mapped[float] = mapped_column(nullable=True)
    duracion_dias: Mapped[int] = mapped_column(nullable=True)
    historial_medico_id: Mapped[int] = mapped_column(ForeignKey('historial_medico.id'), nullable=False)

    historial_medico: Mapped["HistorialMedico"] = relationship(back_populates="tratamientos")
