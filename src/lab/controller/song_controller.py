from http import HTTPStatus
from fastapi import APIRouter
from fastapi.params import Depends
from lab.domain.models_domain import Song
from lab.repository.song_repository import SongRepository, ISongRepository
from lab.repository.models_repository import SongEntity

api_router = APIRouter(prefix="/song", tags=["song"])


@api_router.post("", status_code=HTTPStatus.CREATED)
def create_song(
    song: Song, repository: ISongRepository = Depends(SongRepository)
) -> Song:
    created_song = repository.create(
        SongEntity(
            title=song.title,
            artist_id=song.artist_id,
            album=song.album,
            year=song.year,
        ),
    )

    return Song(
        id=created_song.id,
        title=created_song.title,
        artist_id=created_song.artist.id,
        album=created_song.album,
        year=created_song.year,
        created_at=created_song.created_at,
    )


@api_router.get("")
def query_song(
    name_filter: str = "", repository: ISongRepository = Depends(SongRepository)
) -> list[Song]:
    return repository.query(name_filter)
