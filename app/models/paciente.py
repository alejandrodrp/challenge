from sqlalchemy import Column, Integer, String, Date

from mixins import SoftDeleteMixin, TimestampMixin, Base


class Paciente(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "paciente"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    direccion = Column(String(255), nullable=True)
    telefono = Column(String(20), nullable=True)
    email = Column(String(100), unique=True, nullable=True)