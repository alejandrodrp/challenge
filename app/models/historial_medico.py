from datetime import datetime
from typing import List

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.database import Base
# from app.models import Paciente, Tratamiento
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class HistorialMedico(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "historial_medico"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    diagnostico: Mapped[str] = mapped_column(String(255), nullable=False)
    tratamiento: Mapped[str] = mapped_column(String(255), nullable=True)
    fecha_registro: Mapped[datetime] = mapped_column(default=datetime.now())
    paciente_id: Mapped[int] = mapped_column(Integer, ForeignKey('paciente.id'), nullable=False)

    paciente: Mapped["Paciente"] = relationship(back_populates="historial_medico")
    tratamientos: Mapped[List["Tratamiento"]] = relationship(back_populates="historial_medico")
