import logging

import psycopg2
import sys
from core import lifespan
from fastapi import FastAPI
import subprocess
from core import system

logger = logging.getLogger(__name__)

app = FastAPI(
    title="v-manager",
    version="1.0.0",
    description="alex1000v",
    openapi_url="/openapi.json",
    docs_url="/docs",
)

psycopg2.pool

@app.get("/system/uptime")
async def get_uptime():
    return system.uptime()

@app.get("/system/freeozu")
async def get_free_ozu():
    return system.get_free_ozu()
