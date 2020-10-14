
import click

from euchrecli.util import output
from euchrecli.util.config_util import read_config_file, update_config_file, \
    print_config


@click.group(
    help='Configure and personalize euchre-cli.'
)
@click.help_option(
    '-h', '--help'
)
def config():
    pass


@click.command(
    help='Get all user set euchre-cli configs.'
)
@click.help_option(
    '-h', '--help'
)
def get():
    config = read_config_file()

    for k, v in config.items():
        print(f'\t{k:<24}{v}')


@click.command(
    help='Set a euchre-cli config value.'
)
@click.help_option(
    '-h', '--help'
)
@click.argument(
    'key'
)
@click.argument(
    'value'
)
def set(key: str, value: str):
    config = read_config_file()

    if key not in config:
        output(f'\tError: {key} is not a valid config.', delay=0)
        return

    config[key] = value

    update_config_file(config)
    print(f'set: {key}, {value}')


@click.command(
    help='Reset a euchre-cli config value to its default.'
)
@click.help_option(
    '-h', '--help'
)
@click.argument(
    'key',
    required=False
)
def reset(key: str):
    print(f'reset: {key}')


config.add_command(get, 'get')
config.add_command(set, 'set')
config.add_command(reset, 'reset')
