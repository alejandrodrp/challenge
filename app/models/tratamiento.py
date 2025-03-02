from sqlalchemy import Column, String, Integer, Float

from app.core.database import Base
from app.models.mixins import SoftDeleteMixin, TimestampMixin


class Tratamiento(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "tratamiento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    costo_estimado = Column(Float, nullable=True)
    duracion_dias = Column(Integer, nullable=True)
