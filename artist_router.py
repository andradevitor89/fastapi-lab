from fastapi import APIRouter
from api_models import Artist
import artist_db
from db_models import ArtistEntity

api_router = APIRouter(prefix="/artist", tags=["artist"])


@api_router.post("")
def create(artist: Artist) -> Artist:
    created_artist = artist_db.create(ArtistEntity(
        name=artist.name,
        country=artist.country
    ))

    return Artist(
        id=created_artist.id,
        name=created_artist.name,
        created_at=created_artist.created_at,
        country=created_artist.country
    )


@api_router.get("")
def query(name_filter: str = "") -> list[Artist]:
    return artist_db.query(name_filter)
