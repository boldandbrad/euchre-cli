
from click.testing import CliRunner

from euchrecli.euchre import cli


def test_play():
    runner = CliRunner()
    result = runner.invoke(cli, ['play', '-w'])
    assert result.exit_code == 0
