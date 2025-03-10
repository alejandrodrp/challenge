from datetime import date
from typing import List
from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin
# from app.models.doctor import Doctor
# from app.models.paciente import Paciente


class Cita(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "cita"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    fecha: Mapped[date] = mapped_column(nullable=False)
    hora: Mapped[str] = mapped_column(String(10), nullable=False)
    motivo: Mapped[str] = mapped_column(String(255), nullable=False)
    estado: Mapped[str] = mapped_column(String(50), default="pendiente")  # pendiente, completada, cancelada
    costo: Mapped[float] = mapped_column(nullable=False)
    paciente_id: Mapped[int] = mapped_column(ForeignKey('paciente.id'), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey('doctor.id'), nullable=False)

    paciente: Mapped["Paciente"] = relationship(
        back_populates="citas")
    doctor: Mapped[List["Doctor"]] = relationship(
        back_populates="citas")
