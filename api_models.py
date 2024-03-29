from datetime import datetime
from pydantic import BaseModel


class Song(BaseModel):
    id: int = None
    title: str
    artist: str
    album: str
    year: int
    created_at: datetime = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Car",
                "artist": "Arctic Monkeys",
                "album": "The Car",
                "year": 2022
            }
        }


class Artist(BaseModel):
    id: int = None
    name: str
    created_at: datetime = None
    country: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Arctic Monkeys",
                "country": "UK"
            }
        }
