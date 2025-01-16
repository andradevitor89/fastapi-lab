from abc import abstractmethod, ABC
from lab.repository.db import get_db
from lab.repository.models_repository import ArtistEntity
from sqlalchemy.exc import SQLAlchemyError


class IArtistRepository(ABC):
    @abstractmethod
    def create(self, artist: ArtistEntity) -> ArtistEntity:
        """Create a new artist record."""
        pass

    @abstractmethod
    def query(self, name_filter: str = "") -> list[ArtistEntity]:
        """Query artist records by name filter."""
        pass


class ArtistRepository(IArtistRepository):

    def create(self, artist: ArtistEntity) -> ArtistEntity:
        """Create a new artist record in the database."""
        try:
            with get_db() as db:
                db.add(artist)
                db.commit()
                db.refresh(artist)
                return artist
        except SQLAlchemyError as e:
            db.rollback()
            raise RuntimeError(f"Error creating artist: {e}")

    def query(self, name_filter: str = "") -> list[ArtistEntity]:
        """Query artist records by name filter."""
        try:
            with get_db() as db:
                return (
                    db.query(ArtistEntity)
                    .filter(ArtistEntity.name.ilike(f"%{name_filter}%"))
                    .all()
                )
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error querying artists: {e}")
