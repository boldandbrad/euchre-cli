
import click

from euchrecli.command.play import play


@click.group()
@click.version_option()
def cli():
    """euchre cli main command group.
    """
    pass


cli.add_command(play, 'play')


if __name__ == "__main__":
    cli()
