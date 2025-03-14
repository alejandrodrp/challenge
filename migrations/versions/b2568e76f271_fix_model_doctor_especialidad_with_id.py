"""fix: model doctor_especialidad with id

Revision ID: b2568e76f271
Revises: 16ba1bcd6de1
Create Date: 2025-03-05 00:52:47.432589

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2568e76f271'
down_revision: Union[str, None] = '16ba1bcd6de1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Eliminar las claves primarias existentes
    op.drop_constraint('doctor_especialidad_pkey', 'doctor_especialidad', type_='primary')

    # Añadir la nueva columna id con SQL en bruto
    op.execute('ALTER TABLE doctor_especialidad ADD COLUMN id SERIAL PRIMARY KEY')

   # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Eliminar la clave primaria actual
    op.drop_constraint('doctor_especialidad_pkey', 'doctor_especialidad', type_='primary')

    # Eliminar la columna id con SQL en bruto
    op.execute('ALTER TABLE doctor_especialidad DROP COLUMN id')

    # Volver a establecer doctor_id y especialidad_id como claves primarias
    op.create_primary_key('doctor_especialidad_pkey', 'doctor_especialidad', ['doctor_id', 'especialidad_id'])
    # ### end Alembic commands ###
