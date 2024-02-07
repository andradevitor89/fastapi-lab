from fastapi import APIRouter
from api_models import Song
import db
from db_models import SongEntity

api_router = APIRouter(prefix="/song", tags=["song"])


@api_router.post("")
def create_song(song: Song) -> Song:
    created_song = db.create_song(SongEntity(
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
def query_song(name_filter: str = "") -> list[Song]:
    return db.query_song(name_filter)
    return []
