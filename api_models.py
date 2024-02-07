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
