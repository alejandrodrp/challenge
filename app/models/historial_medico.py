from datetime import datetime

from sqlalchemy import Column, String, Integer, Date

from mixins import SoftDeleteMixin, TimestampMixin, Base


class HistorialMedico(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "historial_medico"

    id = Column(Integer, primary_key=True, autoincrement=True)
    diagnostico = Column(String(255), nullable=False)
    tratamiento = Column(String(255), nullable=True)
    fecha_registro = Column(Date, default=datetime.date.today)