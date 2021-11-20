from click.testing import CliRunner

from euchre.euchre import cli


def test_play():
    runner = CliRunner()
    result = runner.invoke(cli, ["play", "-w"])
    assert result.exit_code == 0
