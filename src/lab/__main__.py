import click

from lab.cli.db_cli import db_commands


@click.group()
def cli():
    """Initialize"""


cli.add_command(db_commands)

if __name__ == "__main__":
    cli()
