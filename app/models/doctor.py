from sqlalchemy import Column, String, Integer, Boolean

from mixins import SoftDeleteMixin, TimestampMixin, Base


class Doctor(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=True)
    email = Column(String(100), unique=True, nullable=True)
    licencia_medica = Column(String(50), unique=True, nullable=False)
    activo = Column(Boolean, default=True)
