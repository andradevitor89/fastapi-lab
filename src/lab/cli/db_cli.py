from lab.repository.models_repository import Base
import lab.repository.db as db
import click


@click.group(name="db")
def db_commands():
    """Command group for data base chores and commands."""


@db_commands.command(name="recreate")
def recreate_db():
    print("Dropping and creating tables")
    Base.metadata.drop_all(db.engine)
    Base.metadata.create_all(db.engine)
    print("Tables created")
