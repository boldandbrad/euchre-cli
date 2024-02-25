from click.testing import CliRunner

from euchre.root import cli


def test_play():
    result = CliRunner().invoke(cli, ["play", "-w"])
    assert result.exit_code == 0
