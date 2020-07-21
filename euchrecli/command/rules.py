
import webbrowser

import click


@click.command(
    help='Open euchre-cli rules docs in web browser.'
)
def rules():
    rules_url = 'https://bradleycwojcik.github.io/euchre-cli/#/rules'
    print(f'\tOpening {rules_url} ...')
    webbrowser.open_new_tab(rules_url)
