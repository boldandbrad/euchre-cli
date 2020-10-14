
import click

from euchrecli.command.config import config
from euchrecli.command.play import play
from euchrecli.command.rules import rules
from euchrecli.util.config_util import config_init
from euchrecli.util.env_util import os_file_paths
from euchrecli.util.log_util import logger_init


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
    config_path, log_path = os_file_paths()

    config_init(config_path)
    logger_init(log_path)


# available sub commands
cli.add_command(config, 'config')
cli.add_command(play, 'play')
cli.add_command(rules, 'rules')


if __name__ == "__main__":
    cli()
