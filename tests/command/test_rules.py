
from click.testing import CliRunner
from pytest_mock import mocker

from euchrecli.euchre import cli


def test_rules(mocker):
    mocker.patch('builtins.input', side_effect=['n'])

    runner = CliRunner()
    result = runner.invoke(cli, ['rules'])
    assert result.exit_code == 0
