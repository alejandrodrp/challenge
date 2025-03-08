from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
# from app.models import Doctor, Especialidad
from app.models.mixins import TimestampMixin, SoftDeleteMixin


class DoctorEspecialidad(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = 'doctor_especialidad'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey('doctor.id'), primary_key=True)
    especialidad_id: Mapped[int] = mapped_column(ForeignKey('especialidad.id'), primary_key=True)

    doctor: Mapped["Doctor"] = relationship(back_populates="especialidades")
    especialidad: Mapped["Especialidad"] = relationship(back_populates="doctores")
