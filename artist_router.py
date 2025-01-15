from http import HTTPStatus
from fastapi import APIRouter
from fastapi.params import Depends
from api_models import Artist
import artist_db
from db import get_db
from db_models import ArtistEntity
from sqlalchemy.orm import Session

api_router = APIRouter(prefix="/artist", tags=["artist"])


@api_router.post("", status_code=HTTPStatus.CREATED)
def create(artist: Artist, db: Session = Depends(get_db)) -> Artist:
    created_artist = artist_db.create(
        db, ArtistEntity(name=artist.name, country=artist.country)
    )

    return Artist(
        id=created_artist.id,
        name=created_artist.name,
        created_at=created_artist.created_at,
        country=created_artist.country,
    )


@api_router.get("")
def query(name_filter: str = "", db: Session = Depends(get_db)) -> list[Artist]:
    return artist_db.query(db, name_filter)
