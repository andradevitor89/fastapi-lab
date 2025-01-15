from fastapi import FastAPI
from lab.controller.song_controller import api_router as song_api_router
from lab.controller.artist_controller import api_router as artist_api_router


app = FastAPI()

app.include_router(song_api_router)
app.include_router(artist_api_router)
