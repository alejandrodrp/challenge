from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base
from app.models.mixins import TimestampMixin, SoftDeleteMixin

class User(Base, SoftDeleteMixin, TimestampMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)