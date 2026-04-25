import logging

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.lifespan import lifespan
from app.database_session import new_async_session
from app.models import MemoryLog
from app.core import system

logger = logging.getLogger(__name__)

app = FastAPI(
    title="v-manager",
    version="1.0.0",
    description="Created by alex1000v",
    docs_url="/docs",
    lifespan=lifespan
)

@app.get("/system/uptime")
async def get_uptime():
    return system.uptime()

@app.get("/system/freeozu")
async def get_freeozu(session: AsyncSession = Depends(new_async_session)):
    value = system.get_free_ozu()
    new_log = MemoryLog(free_value=float(value))
    session.add(new_log)
    await session.commit()
    
    return {"free_mb": value}
