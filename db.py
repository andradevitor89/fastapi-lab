from sqlalchemy import create_engine
from sqlalchemy.engine import URL

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
