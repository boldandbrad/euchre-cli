
import click

from euchrecli.command.play import play
from euchrecli.command.rules import rules


@click.group(
    help='Play euchre in your terminal.'
)
@click.help_option(
    '-h', '--help'
)
@click.version_option(
    None,  # use version auto discovery via setuptools
    '-v', '--version',
    message='%(prog)s-cli, v%(version)s'
)
def cli():
    """Main 'euchre' command group.
    """
    pass


# available sub commands
cli.add_command(play, 'play')
cli.add_command(rules, 'rules')


if __name__ == "__main__":
    cli()
