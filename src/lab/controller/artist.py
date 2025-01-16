from http import HTTPStatus
from fastapi import APIRouter
from fastapi.params import Depends
from lab.domain import api_models, models
from lab.use_cases import (
    CreateArtistUseCase,
    ICreateArtistUseCase,
    IListArtistsUseCase,
    ListArtistsUseCase,
)

artist_api_router = APIRouter(prefix="/artist", tags=["artist"])


@artist_api_router.post("", status_code=HTTPStatus.CREATED)
def create(
    create_artist: api_models.CreateArtist,
    use_case: ICreateArtistUseCase = Depends(CreateArtistUseCase),
) -> api_models.Artist:
    artist: models.Artist = use_case.execute(create_artist)

    return api_models.Artist(
        id=artist.id,
        name=artist.name,
        created_at=artist.created_at,
        country=artist.country,
    )


@artist_api_router.get("")
def query(
    name_filter: str = "", use_case: IListArtistsUseCase = Depends(ListArtistsUseCase)
) -> list[api_models.Artist]:
    artists = use_case.execute(name_filter)
    return [
        api_models.Artist(
            country=artist.country,
            id=artist.id,
            created_at=artist.created_at,
            name=artist.name,
        )
        for artist in artists
    ]
