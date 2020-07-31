
from click.testing import CliRunner

from euchrecli.euchre import cli


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0


def test_help():
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
