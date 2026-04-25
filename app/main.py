import logging

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import new_async_session
from app.models import MemoryLog
from app.core import system
import sys
import os
print(f"Текущая директория: {os.getcwd()}")
print(f"Пути поиска модулей: {sys.path}")

logger = logging.getLogger(__name__)

app = FastAPI(
    title="v-manager",
    version="1.0.0",
    description="Created by alex1000v",
    docs_url="/docs",
)

@app.get("/system/uptime")
async def get_uptime():
    return system.uptime()

@app.get("/system/freeozu")
async def get_freeozu(session: AsyncSession = Depends(new_async_session)):
    new_log = MemoryLog(free_value=get_freeozu)
    session.add(new_log)
    await session.commit()
    return system.get_free_ozu()
