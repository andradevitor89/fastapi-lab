from lab.repository import models
import lab.repository.db as db
import click


@click.group(name="db")
def db_commands():
    """Command group for data base chores and commands."""


@db_commands.command(name="recreate")
def recreate_db():
    print("Dropping and creating tables")
    models.Base.metadata.drop_all(db.engine)
    models.Base.metadata.create_all(db.engine)
    print("Tables created")
