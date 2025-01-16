from abc import ABC, abstractmethod
from lab.repository.db import get_db
from lab.repository.models_repository import SongEntity
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload


class ISongRepository(ABC):
    @abstractmethod
    def create(self, song: SongEntity) -> SongEntity:
        """Create a new song record."""
        pass

    @abstractmethod
    def query(self, name_filter: str = "") -> list[SongEntity]:
        """Query song records by name filter."""
        pass


class SongRepository(ISongRepository):

    def create(self, song: SongEntity) -> SongEntity:
        """Create a new song record in the database."""
        try:
            with get_db() as db:
                db.add(song)
                db.commit()
                db.refresh(song, attribute_names=["artist"])
                return song
        except SQLAlchemyError as e:
            db.rollback()
            raise RuntimeError(f"Error creating song: {e}")

    def query(self, name_filter: str = "") -> list[SongEntity]:
        """Query song records by name filter."""
        try:
            with get_db() as db:
                return (
                    db.query(SongEntity)
                    .options(joinedload(SongEntity.artist))
                    .filter(SongEntity.title.ilike(f"%{name_filter}%"))
                    .all()
                )
        except SQLAlchemyError as e:
            raise RuntimeError(f"Error querying songs: {e}")
