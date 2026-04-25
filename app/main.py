import logging

from fastapi import FastAPI
logger = logging.getLogger(__name__)

app = FastAPI(
    title="v-manager",
    version="1.0.0",
    description="alex1000v",
    openapi_url="/openapi.json",
    docs_url="/docs",
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
