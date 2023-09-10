from fastapi import FastAPI
from .routes.album import album_router

app = FastAPI()

app.include_router(album_router)