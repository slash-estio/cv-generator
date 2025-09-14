import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

static_path = os.path.join(os.path.dirname(__file__), "static")

app.mount("/static", StaticFiles(directory=static_path), name="static")


@app.get("/")
async def index():
    return FileResponse(os.path.join(static_path, "index.html"))
