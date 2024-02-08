from sqlalchemy.orm import Session
from db_models import SongEntity


def create_song(db: Session, song: SongEntity) -> SongEntity:
    db.add(song)
    db.commit()

    return SongEntity(title=song.title, artist=song.artist, album=song.album, year=song.year, created_at=song.created_at, id=song.id)


def query_song(db: Session, name_filter: str = "", ) -> list[SongEntity]:
    return db.query(SongEntity).filter(SongEntity.title.ilike(f"%{name_filter}%")).all()
