from typing import List

from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.core.database import Base
# from app.models import Paciente
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class SeguroMedico(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "seguro_medico"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    cobertura: Mapped[str] = mapped_column(String(255), nullable=True)
    contacto: Mapped[str] = mapped_column(String(100), nullable=True)

    pacientes: Mapped[List["Paciente"]] = relationship(
        back_populates="seguro_medico")
