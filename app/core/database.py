from os import getenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator


DATABASE_URL = "postgresql+asyncpg://%s:%s@%s:%s/%s".format(
    getenv('DB_USER'),
    getenv('DB_PASSWORD'),
    getenv('DB_HOST'),
    getenv('DB_PORT'),
    getenv('DB_NAME')
)

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Dependencia para obtener una sesión asíncrona en los endpoints
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
        