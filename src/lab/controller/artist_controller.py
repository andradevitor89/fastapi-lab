from http import HTTPStatus
from fastapi import APIRouter
from fastapi.params import Depends
from lab.domain.models_domain import Artist

from lab.repository.artist_repository import ArtistRepository, IArtistRepository
from lab.repository.models_repository import ArtistEntity

api_router = APIRouter(prefix="/artist", tags=["artist"])


@api_router.post("", status_code=HTTPStatus.CREATED)
def create(
    artist: Artist, repository: IArtistRepository = Depends(ArtistRepository)
) -> Artist:
    created_artist = repository.create(
        ArtistEntity(name=artist.name, country=artist.country)
    )

    return Artist(
        id=created_artist.id,
        name=created_artist.name,
        created_at=created_artist.created_at,
        country=created_artist.country,
    )


@api_router.get("")
def query(
    name_filter: str = "", repository: IArtistRepository = Depends(ArtistRepository)
) -> list[Artist]:
    return repository.query(name_filter)
