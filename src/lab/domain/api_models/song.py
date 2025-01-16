from datetime import datetime
from pydantic import BaseModel
from lab.domain.api_models import Artist


class SongBase(BaseModel):
    title: str
    album: str
    year: int


class Song(SongBase):
    id: int
    created_at: datetime
    artist: Artist


class CreateSong(SongBase):
    artist_id: int

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Car",
                "artist_id": 1,
                "album": "The Car",
                "year": 2022,
            }
        }
