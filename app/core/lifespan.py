from contextlib import asynccontextmanager
from app.database_session import _ASYNC_ENGINE
from app.models import Base, MemoryLog

@asynccontextmanager
async def lifespan(app):   
    async with _ASYNC_ENGINE.begin() as conn:  
        await conn.run_sync(Base.metadata.create_all)
    yield
