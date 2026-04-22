import ssl
from sqlmodel import text
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
        statement = text("SELECT 'Hello';")
        result = await conn.execute(statement)
        print(result.all())