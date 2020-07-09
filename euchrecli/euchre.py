
import click

from euchrecli.commands.play import play


@click.group()
@click.version_option()
def cli():
    pass


cli.add_command(play, 'play')


if __name__ == "__main__":
    cli()
