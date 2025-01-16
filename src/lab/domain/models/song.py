from datetime import datetime
from pydantic import BaseModel
from lab.domain.models import Artist


class Song(BaseModel):
    id: int
    title: str
    artist_id: int
    album: str
    year: int
    created_at: datetime
    artist: Artist

    class Config:
        from_attributes = True
