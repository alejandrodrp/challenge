import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.auth import get_password_hash
from app.models.user import User
from app.core.database import async_session

async def create_superuser(username: str, email: str, password: str):
    async with async_session() as session:
        async with session.begin():
            hashed_password = get_password_hash(password)
            superuser = User(
                username=username,
                email=email,
                hashed_password=hashed_password,
                is_active=True,
                is_superuser=True
            )
            session.add(superuser)
        await session.commit()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python create_superuser.py <username> <email> <password>")
    else:
        username, email, password = sys.argv[1], sys.argv[2], sys.argv[3]
        asyncio.run(create_superuser(username, email, password))