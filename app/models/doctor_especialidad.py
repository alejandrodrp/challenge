from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base

doctor_especialidad = Table(
    'doctor_especialidad',
    Base.metadata,
    Column('doctor_id', Integer, ForeignKey('doctor.id'), primary_key=True),
    Column('especialidad_id', Integer, ForeignKey('especialidad.id'), primary_key=True)
)