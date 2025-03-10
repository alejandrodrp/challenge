from datetime import datetime
from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.core.database import Base
# from app.models import SeguroMedico, Cita, HistorialMedico
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class Paciente(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "paciente"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    apellido: Mapped[str] = mapped_column(String(100), nullable=False)
    fecha_nacimiento: Mapped[datetime] = mapped_column(nullable=False)
    direccion: Mapped[str] = mapped_column(String(255), nullable=True)
    telefono: Mapped[str] = mapped_column(String(20), nullable=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    seguro_medico_id: Mapped[int] = mapped_column(ForeignKey('seguro_medico.id'), nullable=True)

    seguro_medico: Mapped["SeguroMedico"] = relationship(
        back_populates="pacientes")
    citas: Mapped[List["Cita"]] = relationship(
        back_populates="paciente")
    historial_medico: Mapped["HistorialMedico"] = relationship(
        back_populates="paciente")
