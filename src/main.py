from fastapi import FastAPI
from lab.controller import song_api_router, artist_api_router


app = FastAPI()

app.include_router(song_api_router)
app.include_router(artist_api_router)
