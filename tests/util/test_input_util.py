
import pytest
from pytest_mock import mocker

from euchrecli.util.input_util import int_input


def test_int_input_exception(mocker):
    # not an integer, reprompt
    mocker.patch('builtins.input', side_effect=['Name', 0])
    int_1 = int_input('prompt', 2)
    assert int_1 in range(2)

    # out of range, reprompt
    mocker.patch('builtins.input', side_effect=[5, 0])
    int_2 = int_input('prompt', 2)
    assert int_2 in range(2)
