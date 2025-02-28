import datetime
from sqlalchemy import Column, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base


class SoftDeleteMixin:
    """Mixin para implementar soft delete, evitando la eliminación física."""
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    def soft_delete(self):
        """Marca el registro como eliminado y asigna la fecha actual."""
        self.is_deleted = True
        self.deleted_at = datetime.datetime.now()


class TimestampMixin:
    """Mixin para gestionar los campos de timestamps: created_at y updated_at."""
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


Base = declarative_base()