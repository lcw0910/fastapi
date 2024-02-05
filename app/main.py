import os
import time
from datetime import datetime
from typing import Optional

import uvicorn
from fastapi import FastAPI, Header
from fastapi.openapi.utils import get_openapi
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.core.conf import settings

# Activate this when doing remote debugging.
# import pydevd_pycharm
# pydevd_pycharm.settrace('host.docker.internal', port=12345, stdoutToServer=True, stderrToServer=True)


app = FastAPI(title="FastAPI Example")

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
def read_root():
    envs = os.environ

    APPS_ENV = settings.APPS_ENV
    DEBUG = settings.DEBUG
    APP_NAME = settings.APP_NAME
    APP_BASE_DOMAIN = settings.APP_BASE_DOMAIN

    return {
        "Hello": "World",
    }


@app.get("/stream")
async def stream(token: Optional[str] = Header(None)):

    timeout = 5
    connected_time = datetime.now()

    def check_for_event():
        if (datetime.now() - connected_time).seconds > timeout:
            return "SUCCESS"
        return False

    def event_stream():
        count = 0
        while True:
            if check_for_event() == "SUCCESS":
                yield f"data: {count}\n\n"

            time.sleep(1)
            count += 1

            if count > 10:
                return

    generator = event_stream()
    return StreamingResponse(generator, media_type="text/event-stream")


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


openapi_schema = get_openapi(
    title="Custom title",
    version="0.0.1",
    description="This is a very custom OpenAPI schema",
    routes=app.routes,
    servers=[
        {
            "url": "http://yicheolwon.org",
            "description": "Local",
        },
        {
            "url": "https://api.example.com",
            "description": "Production server",
        },
    ]
)

app.openapi_schema = openapi_schema

if __name__ == "__main__":
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=443,
        reload=True,
        ssl_keyfile="/Users/cwlee02/Project/2024/fastapi-sse/docker/nginx/ssl/key.pem",
        ssl_certfile="/Users/cwlee02/Project/2024/fastapi-sse/docker/nginx/ssl/cert.pem",
    )
