from http import HTTPStatus
from fastapi import APIRouter
from fastapi.params import Depends
from lab.domain import api_models
from lab.use_cases import (
    CreateSongUseCase,
    ICreateSongUseCase,
    IListSongsUseCase,
    ListSongsUseCase,
)

song_api_router = APIRouter(prefix="/song", tags=["song"])


@song_api_router.post("", status_code=HTTPStatus.CREATED)
def create_song(
    create_song: api_models.CreateSong,
    use_case: ICreateSongUseCase = Depends(CreateSongUseCase),
) -> api_models.Song:
    song = use_case.execute(create_song)

    return api_models.Song(
        id=song.id,
        title=song.title,
        album=song.album,
        year=song.year,
        created_at=song.created_at,
        artist=api_models.Artist(
            id=song.artist.id,
            name=song.artist.name,
            country=song.artist.country,
            created_at=song.artist.created_at,
        ),
    )


@song_api_router.get("")
def query_song(
    name_filter: str = "", use_case: IListSongsUseCase = Depends(ListSongsUseCase)
) -> list[api_models.Song]:
    songs = use_case.execute(name_filter)
    return [
        api_models.Song(
            id=song.id,
            title=song.title,
            album=song.album,
            year=song.year,
            created_at=song.created_at,
            artist=api_models.Artist(
                id=song.artist.id,
                name=song.artist.name,
                country=song.artist.country,
                created_at=song.artist.created_at,
            ),
        )
        for song in songs
    ]
