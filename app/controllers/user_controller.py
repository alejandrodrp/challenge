from typing import Type, Dict
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from app.core.auth import get_current_active_user
from app.models.user import User
from app.views.user import UserPublic
from app.core.database import get_session
from app.controllers.base_controller import BaseController

class UserController(BaseController[User, UserPublic]):
    def __init__(self, model: Type[User], schemas: Dict[str, Dict[str, Type[UserPublic]]]):
        super().__init__(model, schemas)

    def _add_routes(self):
        @self.router.delete("/{item_id}", response_model=self._get_schema("delete", "output"))
        async def delete_item(item_id: int, db: AsyncSession = Depends(get_session), soft: bool = True, current_user: UserPublic = Depends(get_current_active_user)):
            if not current_user.is_superuser:
                raise HTTPException(status_code=403, detail="Only superusers can delete users")
            db_item = await self.repository.get(db, id=item_id)
            if db_item is None:
                raise HTTPException(status_code=404, detail="User not found")
            if soft:
                db_item.is_deleted = True
                db_item.deleted_at = func.now()
                db.add(db_item)
                await db.commit()
                await db.refresh(db_item)
                return db_item
            
            return await self.repository.remove(db, id=item_id)

        super()._add_routes()