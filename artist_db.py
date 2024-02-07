from sqlalchemy.orm import sessionmaker
from db_models import ArtistEntity
from db import engine


def create(artist: ArtistEntity) -> ArtistEntity:
    session = sessionmaker(bind=engine)()
    session.add(artist)
    session.commit()

    return ArtistEntity(created_at=artist.created_at, id=artist.id, name=artist.name)


def query(name_filter: str = "") -> list[ArtistEntity]:
    session = sessionmaker(bind=engine)()
    return session.query(ArtistEntity).filter(ArtistEntity.name.ilike(f"%{name_filter}%")).all()
