import click

from euchrecli.game import setup

@click.command()
def cli():
    setup()


if __name__ == "__main__":
    cli()
