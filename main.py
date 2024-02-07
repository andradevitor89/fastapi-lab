from fastapi import FastAPI
from song_router import api_router as song_api_router
import db
from db_models import Base

app = FastAPI()

Base.metadata.create_all(db.engine)


@app.get("/")
def index():
    return {"message": "Hello, World"}


@app.get("/healthcheck")
def healthcheck():
    return db.healthcheck()


app.include_router(song_api_router)
