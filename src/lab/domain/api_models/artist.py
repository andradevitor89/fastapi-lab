from datetime import datetime
from pydantic import BaseModel


class ArtistBase(BaseModel):
    name: str
    country: str


class Artist(ArtistBase):
    id: int
    created_at: datetime


class CreateArtist(ArtistBase):
    class Config:
        json_schema_extra = {"example": {"name": "Arctic Monkeys", "country": "UK"}}
