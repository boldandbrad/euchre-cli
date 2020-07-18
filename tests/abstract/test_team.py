
from euchrecli.abstract import Team


def test_team():
    team = Team('team 1')
    assert team.name == 'team 1'
    assert team.game_score == 0
    assert team.called_trump is False
    assert team.trick_score == 0
    assert team.__repr__() == 'Team(team 1)'
    assert team.__str__() == 'team 1'


def test_won_hand():
    team = Team('team 1')
    team.won_hand(2)
    assert team.game_score == 2


def test_won_trick():
    team = Team('team 1')
    team.won_trick()
    assert team.trick_score == 1
