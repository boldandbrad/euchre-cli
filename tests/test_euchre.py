from click.testing import CliRunner

from euchre.root import cli


def test_version():
    result = CliRunner().invoke(cli, ["--version"])
    assert result.exit_code == 0


def test_help():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0
