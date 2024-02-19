from click.testing import CliRunner

from euchre.root import cli


def test_play():
    runner = CliRunner()
    result = runner.invoke(cli, ["play", "-w"])
    assert result.exit_code == 0
