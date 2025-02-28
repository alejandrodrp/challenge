from sqlalchemy import Column, String, Integer

from mixins import SoftDeleteMixin, TimestampMixin, Base


class Especialidad(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = "especialidad"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)

