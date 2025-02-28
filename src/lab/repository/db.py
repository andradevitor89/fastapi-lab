from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="localhost",
    port=5432,
    database="postgres",
)

engine = create_engine(url)
connection = engine.connect()


@contextmanager
def get_db():
    db = sessionmaker(bind=engine)()
    try:
        yield db
    finally:
        db.close()
