from sqlalchemy.orm import sessionmaker
from db_models import SongEntity
from db import engine


def create_song(song: SongEntity) -> SongEntity:
    session = sessionmaker(bind=engine)()
    session.add(song)
    session.commit()

    return SongEntity(title=song.title, artist=song.artist, album=song.album, year=song.year, created_at=song.created_at, id=song.id)


def query_song(name_filter: str = "") -> list[SongEntity]:
    session = sessionmaker(bind=engine)()
    return session.query(SongEntity).filter(SongEntity.title.ilike(f"%{name_filter}%")).all()
