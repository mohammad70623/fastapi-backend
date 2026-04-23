import ssl
from sqlmodel import text, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from src.config import config
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
                         
ssl_context = ssl.create_default_context()

engine = create_async_engine(
    url=config.DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context}
)

async def init_db() ->None:
    async with engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session()->AsyncSession:
    Session = sessionmaker(
        bind = engine,
        class_ = AsyncSession,
        expire_on_commit=False
    ) 
    async with Session() as session:
        yield session 
