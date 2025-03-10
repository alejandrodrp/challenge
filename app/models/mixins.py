from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class SoftDeleteMixin:
    """Mixin para implementar soft delete, evitando la eliminación física."""
    is_deleted: Mapped[bool] = mapped_column(default=False, nullable=False)
    deleted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    def soft_delete(self):
        """Marca el registro como eliminado y asigna la fecha actual."""
        self.is_deleted = True
        self.deleted_at = datetime.now()


class TimestampMixin:
    """Mixin para gestionar los campos de timestamps: created_at y updated_at."""
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(), onupdate=func.now())
