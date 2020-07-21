
import click

from euchrecli.command.play import play
from euchrecli.command.rules import rules


@click.group()
@click.version_option()
def cli():
    """Play euchre in your terminal.
    """
    pass


cli.add_command(play, 'play')
cli.add_command(rules, 'rules')


if __name__ == "__main__":
    cli()
