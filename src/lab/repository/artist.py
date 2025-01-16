from abc import abstractmethod, ABC
from lab.repository.db import get_db
from lab.repository import models


class IArtistRepository(ABC):
    @abstractmethod
    def create(self, artist: models.ArtistEntity) -> models.ArtistEntity:
        """Create a new artist record."""

    @abstractmethod
    def query(self, name_filter: str = "") -> list[models.ArtistEntity]:
        """Query artist records by name filter."""


class ArtistRepository(IArtistRepository):

    def create(self, artist: models.ArtistEntity) -> models.ArtistEntity:
        """Create a new artist record in the database."""
        with get_db() as db:
            db.add(artist)
            db.commit()
            db.refresh(artist)
            return artist

    def query(self, name_filter: str = "") -> list[models.ArtistEntity]:
        """Query artist records by name filter."""
        with get_db() as db:
            return (
                db.query(models.ArtistEntity)
                .filter(models.ArtistEntity.name.ilike(f"%{name_filter}%"))
                .all()
            )
