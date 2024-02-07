from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from db_models import SongEntity

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="localhost",
    port=5432,
    database="postgres"
)

engine = create_engine(url)
connection = engine.connect()


def healthcheck() -> bool:
    connection.execute("select * from information_schema.tables;")
    return True


def create_song(song: SongEntity) -> SongEntity:
    session = sessionmaker(bind=engine)()
    session.add(song)
    session.commit()

    return SongEntity(title=song.title, artist=song.artist, album=song.album, year=song.year, created_at=song.created_at, id=song.id)


def query_song(name_filter: str = "") -> list[SongEntity]:
    session = sessionmaker(bind=engine)()
    return session.query(SongEntity).filter(SongEntity.title.ilike(f"%{name_filter}%")).all()
