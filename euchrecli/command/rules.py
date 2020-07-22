
import webbrowser

import click

from euchrecli.util.input_util import bool_input


@click.command(
    help='Open euchre-cli rules page in a web browser.'
)
@click.help_option(
    '-h', '--help'
)
@click.option(
    '-y', '--yes',
    default=False,
    is_flag=True,
    help='Auto confirm to open rules in a browser.'
)
def rules(yes: bool):
    rules_url = 'https://bradleycwojcik.github.io/euchre-cli/#/rules'
    prog_str = click.style('euchre-cli', fg='green')

    if yes or bool_input(f'Open {prog_str} rules page in a browser?'):
        print(click.style(
                f'\tOpening rules at {rules_url} ...',
                fg='bright_black'
            ))
        webbrowser.open(rules_url)
    else:
        print(f'\tRead {prog_str} rules at {rules_url}')
