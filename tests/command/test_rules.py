from click.testing import CliRunner

from euchre.root import cli


def test_rules(mocker):
    mocker.patch("builtins.input", side_effect=["n"])

    result = CliRunner().invoke(cli, ["rules"])
    assert result.exit_code == 0
