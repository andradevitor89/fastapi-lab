from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

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


def get_db():
    db = sessionmaker(bind=engine)()
    try:
        yield db
    finally:
        print("Closing db")
        db.close()
