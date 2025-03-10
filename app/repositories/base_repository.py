from typing import Generic, Type, TypeVar, Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from pydantic import BaseModel


# Define a generic type variable
T = TypeVar('T', bound=BaseModel)
ModelType = TypeVar('ModelType')


class BaseRepository(Generic[ModelType, T]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    async def get(self, db: AsyncSession, id: int, include_deleted: bool = False) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == id)
        if not include_deleted:
            query = query.where(self.model.is_deleted == False)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def get_all(self, db: AsyncSession, page_size: int = 10, page: int = 1, limit: int = None,
                      include_deleted: bool = False) -> Sequence[ModelType]:
        offset = (page - 1) * page_size
        base_query = select(self.model)

        if not include_deleted:
            base_query = base_query.where(self.model.is_deleted == False)

        # Consulta para obtener el total de registros reales
        count_query = select(func.count(self.model.id))
        if not include_deleted:
            count_query = count_query.where(self.model.is_deleted == False)
        if limit:
            count_query = count_query.limit(limit)
        total_result = await db.execute(count_query)
        total_real = total_result.scalar() or 0

        # Se limita el total a lo máximo deseado
        effective_total = min(total_real, limit if limit else total_real)

        # Si el offset es mayor o igual al total efectivo, se devuelve una lista vacía
        if offset >= effective_total:
            return []

        # Determinar el límite para la consulta: si es la última página,
        # current_limit será la cantidad de elementos restantes, de lo contrario, page_size.
        remaining = effective_total - offset
        current_limit = remaining if remaining < page_size else page_size

        # Consulta paginada usando el límite calculado
        paginated_query = base_query.offset(offset).limit(current_limit)
        result = await db.execute(paginated_query)

        return result.scalars().all()

    async def create(self, db: AsyncSession, obj_in: T) -> ModelType:
        obj_in_data = obj_in.model_dump(exclude_unset=True)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, db_obj: ModelType, obj_in: T) -> ModelType:
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def remove(self, db: AsyncSession, id: int) -> ModelType:
        result = await db.execute(select(self.model).filter(self.model.id == id))
        obj = result.scalar_one_or_none()
        if obj is None:
            raise ValueError("Object not found")
        await db.delete(obj)
        await db.commit()
        return obj
