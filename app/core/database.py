from os import getenv
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Construir la URL de la base de datos; se asume que todas las variables de entorno están definidas.
DATABASE_URL: str = (
    f"postgresql+asyncpg://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}"
    f"@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"
)

# Crear el engine asíncrono; se especifica el tipo AsyncEngine.
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

async_session: sessionmaker[AsyncSession] = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


class Base(DeclarativeBase):
    pass
