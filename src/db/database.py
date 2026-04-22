import ssl
from sqlmodel import text, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import config
 
ssl_context = ssl.create_default_context()

engine = create_async_engine(
    url=config.DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context}
)

async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)