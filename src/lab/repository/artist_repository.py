from abc import abstractmethod
from lab.repository.db import get_db
from lab.repository.models_repository import ArtistEntity


class IArtistRepository:
    @abstractmethod
    def create(self, artist: ArtistEntity) -> ArtistEntity:
        pass

    @abstractmethod
    def query(self, name_filter: str = "") -> list[ArtistEntity]:
        pass


class ArtistRepository(IArtistRepository):

    def create(self, artist: ArtistEntity) -> ArtistEntity:
        with get_db() as db:
            db.add(artist)
            db.commit()

            return ArtistEntity(
                created_at=artist.created_at,
                id=artist.id,
                name=artist.name,
                country=artist.country,
            )

    def query(self, name_filter: str = "") -> list[ArtistEntity]:
        with get_db() as db:
            return (
                db.query(ArtistEntity)
                .filter(ArtistEntity.name.ilike(f"%{name_filter}%"))
                .all()
            )
