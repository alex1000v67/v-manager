from contextlib import asynccontextmanager
from app.database_session import engine
from app.models import Base, MemoryLog

@asynccontextmanager
async def lifespan(app):   
    async with engine.begin() as conn:  
        await conn.run_sync(Base.metadata.create_all)
    yield
