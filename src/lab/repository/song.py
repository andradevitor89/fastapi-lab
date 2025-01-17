from abc import ABC, abstractmethod
from lab.repository.db import get_db
from lab.repository import models
from sqlalchemy.orm import joinedload


class ISongRepository(ABC):
    @abstractmethod
    def create(self, song: models.SongEntity) -> models.SongEntity:
        """Create a new song record."""

    @abstractmethod
    def query(self, name_filter: str = "") -> list[models.SongEntity]:
        """Query song records by name filter."""

    @abstractmethod
    def query_by_artist_id(self, artist_id: int) -> list[models.SongEntity]:
        """Query song records by artist id."""


class SongRepository(ISongRepository):

    def create(self, song: models.SongEntity) -> models.SongEntity:
        """Create a new song record in the database."""

        with get_db() as db:
            db.add(song)
            db.commit()
            db.refresh(song, attribute_names=["artist"])
            return song

    def query(self, name_filter: str = "") -> list[models.SongEntity]:
        """Query song records by name filter."""
        with get_db() as db:
            return (
                db.query(models.SongEntity)
                .options(joinedload(models.SongEntity.artist))
                .filter(models.SongEntity.title.ilike(f"%{name_filter}%"))
                .all()
            )

    def query_by_artist_id(self, artist_id: int) -> list[models.SongEntity]:
        """Query song records by artist id."""
        with get_db() as db:
            return (
                db.query(models.SongEntity)
                .filter(models.SongEntity.artist_id == artist_id)
                .all()
            )
