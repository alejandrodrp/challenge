from typing import Generic, Type, TypeVar, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from app.core.database import Base  # Importar Base desde database.py

# Define a generic type variable
T = TypeVar('T', bound=BaseModel)
ModelType = TypeVar('ModelType')


class BaseRepository(Generic[ModelType, T]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: int, include_deleted: bool = False) -> Optional[ModelType]:
        query = select(self.model).filter(self.model.id == id)
        if not include_deleted:
            query = query.filter(self.model.is_deleted == False)
        result = await db.execute(query)
        return result.scalars().first()

    async def get_all(self, db: AsyncSession, skip: int = 0, limit: int = 100, include_deleted: bool = False) -> List[ModelType]:
        query = select(self.model).offset(skip).limit(limit)
        if not include_deleted:
            query = query.filter(self.model.is_deleted == False)
        result = await db.execute(query)
        return result.scalars().all()

    async def create(self, db: AsyncSession, obj_in: T) -> ModelType:
        obj_in_data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, db_obj: ModelType, obj_in: T) -> ModelType:
        obj_data = vars(db_obj)
        update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def remove(self, db: AsyncSession, id: int) -> ModelType:
        result = await db.execute(select(self.model).filter(self.model.id == id))
        obj = result.scalars().first()
        await db.delete(obj)
        await db.commit()
        return obj
