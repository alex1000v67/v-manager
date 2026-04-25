import logging

from fastapi import FastAPI
import subprocess
logger = logging.getLogger(__name__)

app = FastAPI(
    title="v-manager",
    version="1.0.0",
    description="alex1000v",
    openapi_url="/openapi.json",
    docs_url="/docs",
)

@app.get("/system/uptime")
def uptime():
    uptime = subprocess.run("uptime", shell=True, capture_output=True, text=True)
    return {"output": uptime.stdout.strip()}

@app.get("/system/freeozu")
def freeozu():
    ozu = subprocess.run("free -m", shell=True, capture_output=True, text=True)
    return {"output": ozu.stdout.strip()}

