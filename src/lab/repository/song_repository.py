from abc import abstractmethod
from lab.repository.db import get_db
from lab.repository.models_repository import SongEntity


class ISongRepository:
    @abstractmethod
    def create(self, song: SongEntity) -> SongEntity:
        pass

    @abstractmethod
    def query(self, name_filter: str = "") -> list[SongEntity]:
        pass


class SongRepository(ISongRepository):

    def create(self, song: SongEntity) -> SongEntity:
        with get_db() as db:
            db.add(song)
            db.commit()

            return SongEntity(
                title=song.title,
                artist=song.artist,
                album=song.album,
                year=song.year,
                created_at=song.created_at,
                id=song.id,
            )

    def query(self, name_filter: str = "") -> list[SongEntity]:
        with get_db() as db:
            return (
                db.query(SongEntity)
                .filter(SongEntity.title.ilike(f"%{name_filter}%"))
                .all()
            )
