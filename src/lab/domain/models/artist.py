from datetime import datetime
from pydantic import BaseModel


class Artist(BaseModel):
    id: int
    name: str
    created_at: datetime
    country: str

    class Config:
        from_attributes = True
