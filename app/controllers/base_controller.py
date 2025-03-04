from typing import Type, TypeVar, Generic, List, Dict
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, ValidationError

from app.core.database import get_session
from app.repositories.base_repository import BaseRepository, ModelType
from app.core.auth import get_current_active_user
from app.views.user import UserPublic

T = TypeVar('T', bound=BaseModel)
SchemaType = TypeVar('SchemaType', bound=BaseModel)


class BaseController(Generic[ModelType, SchemaType]):
    def __init__(self, model: Type[ModelType], schemas: Dict[str, Dict[str, Type[SchemaType]]]):
        self.model = model
        self.schemas = schemas
        self.router = APIRouter()
        self.repository = BaseRepository[ModelType, SchemaType](model)
        self._add_routes()

    def _get_schema(self, operation: str, schema_type: str) -> Type[SchemaType]:
        return self.schemas.get(operation, {}).get(schema_type)

    def _add_routes(self):
        @self.router.get("/", response_model=List[self._get_schema("get", "output")])
        async def read_items(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session), current_user: UserPublic = Depends(get_current_active_user)):
            return await self.repository.get_all(db, skip=skip, limit=limit)

        @self.router.get("/{item_id}", response_model=self._get_schema("get", "output"))
        async def read_item(item_id: int, db: AsyncSession = Depends(get_session), current_user: UserPublic = Depends(get_current_active_user)):
            db_item = await self.repository.get(db, id=item_id)
            if db_item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return db_item

        @self.router.post("/", response_model=self._get_schema("post", "output"))
        async def create_item(item_in: dict = Body(...), db: AsyncSession = Depends(get_session), current_user: UserPublic = Depends(get_current_active_user)):
            schema = self._get_schema("post", "input")
            try:
                item_in = schema.model_validate(item_in)
            except ValidationError as e:
                raise HTTPException(status_code=422, detail=e.errors())
            db_obj = await self.repository.create(db, obj_in=item_in)
            return self._get_schema("post", "output").model_validate(db_obj)

        @self.router.put("/{item_id}", response_model=self._get_schema("put", "output"))
        async def update_item(item_id: int, item_in: dict = Body(...), db: AsyncSession = Depends(get_session), current_user: UserPublic = Depends(get_current_active_user)):
            schema = self._get_schema("put", "input")
            try:
                item_in = schema.model_validate(item_in)
            except ValidationError as e:
                raise HTTPException(status_code=422, detail=e.errors())
            db_item = await self.repository.get(db, id=item_id)
            if db_item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            db_obj = await self.repository.update(db, db_obj=db_item, obj_in=item_in)
            return self._get_schema("put", "output").model_validate(db_obj)

        @self.router.delete("/{item_id}", response_model=self._get_schema("delete", "output"))
        async def delete_item(item_id: int, db: AsyncSession = Depends(get_session), current_user: UserPublic = Depends(get_current_active_user)):
            db_item = await self.repository.get(db, id=item_id)
            if db_item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return await self.repository.remove(db, id=item_id)
