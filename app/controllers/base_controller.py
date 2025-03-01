from typing import Type, TypeVar, Generic, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.core.database import get_session
from app.repositories.base_repository import BaseRepository, ModelType

T = TypeVar('T', bound=BaseModel)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class BaseController(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], create_schema: Type[CreateSchemaType], update_schema: Type[UpdateSchemaType]):
        self.model = model
        self.create_schema = create_schema
        self.update_schema = update_schema
        self.router = APIRouter()
        self.repository = BaseRepository[ModelType, CreateSchemaType](model)
        self._add_routes()

    def _add_routes(self):
        @self.router.get("/", response_model=List[ModelType])
        def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
            return self.repository.get_all(db, skip=skip, limit=limit)

        @self.router.get("/{item_id}", response_model=ModelType)
        def read_item(item_id: int, db: Session = Depends(get_session)):
            db_item = self.repository.get(db, id=item_id)
            if db_item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return db_item

        @self.router.post("/", response_model=ModelType)
        def create_item(item_in: CreateSchemaType, db: Session = Depends(get_session)):
            return self.repository.create(db, obj_in=item_in)

        @self.router.put("/{item_id}", response_model=ModelType)
        def update_item(item_id: int, item_in: UpdateSchemaType, db: Session = Depends(get_session)):
            db_item = self.repository.get(db, id=item_id)
            if db_item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return self.repository.update(db, db_obj=db_item, obj_in=item_in)

        @self.router.delete("/{item_id}", response_model=ModelType)
        def delete_item(item_id: int, db: Session = Depends(get_session)):
            db_item = self.repository.get(db, id=item_id)
            if db_item is None:
                raise HTTPException(status_code=404, detail="Item not found")
            return self.repository.remove(db, id=item_id)
