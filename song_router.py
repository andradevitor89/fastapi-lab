from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from api_models import Song
from db import get_db
import songs_db
from db_models import SongEntity

api_router = APIRouter(prefix="/song", tags=["song"])


@api_router.post("")
def create_song(song: Song,  db: Session = Depends(get_db)) -> Song:
    created_song = songs_db.create_song(db, SongEntity(
        title=song.title,
        artist=song.artist,
        album=song.album,
        year=song.year,
    ))

    return Song(
        id=created_song.id,
        title=created_song.title,
        artist=created_song.artist,
        album=created_song.album,
        year=created_song.year,
        created_at=created_song.created_at
    )


@api_router.get("")
def query_song(name_filter: str = "", db: Session = Depends(get_db)) -> list[Song]:
    return songs_db.query_song(db, name_filter)
