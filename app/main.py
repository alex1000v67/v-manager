import logging

from fastapi import FastAPI
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
    return uptime()

@app.get("/system/freeozu")
async def get_free_ozu():
    return get_free_ozu()
