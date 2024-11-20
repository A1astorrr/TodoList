from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=False,  # при true позволяет видеть все запросы в консоли
    # pool_size=5, # кол-во подключений к бд
    # max_overflow=10, # доп. слоты для подключения
)

async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

class Base(DeclarativeBase):
    pass
