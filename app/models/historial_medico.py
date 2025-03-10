from datetime import datetime
from typing import List

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from app.core.database import Base
# from app.models import Paciente, Tratamiento
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class HistorialMedico(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "historial_medico"

    id: Mapped[int] = Column(primary_key=True, autoincrement=True)
    diagnostico: Mapped[str] = Column(String(255), nullable=False)
    tratamiento: Mapped[str] = Column(String(255), nullable=True)
    fecha_registro: Mapped[datetime] = Column(default=datetime.now())
    paciente_id: Mapped[int] = Column(Integer, ForeignKey('paciente.id'), nullable=False)

    paciente: Mapped["Paciente"] = relationship(back_populates="historial_medico")
    tratamientos: Mapped[List["Tratamiento"]] = relationship(back_populates="historial_medico")
