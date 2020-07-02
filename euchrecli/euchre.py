import click

from euchrecli.game import setup


@click.group()
@click.version_option()
def cli():
    pass


@cli.command(help='Start a new euchre game.')
def play():
    setup()


if __name__ == "__main__":
    cli()
