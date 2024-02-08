from sqlalchemy.orm import Session
from db_models import ArtistEntity


def create(db: Session, artist: ArtistEntity,) -> ArtistEntity:
    db.add(artist)
    db.commit()

    return ArtistEntity(created_at=artist.created_at, id=artist.id, name=artist.name, country=artist.country)


def query(db: Session, name_filter: str = "",) -> list[ArtistEntity]:
    return db.query(ArtistEntity).filter(ArtistEntity.name.ilike(f"%{name_filter}%")).all()
