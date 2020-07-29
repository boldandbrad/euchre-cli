
from euchrecli.abstract import Player, Team


def test_player():
    team = Team('Team')
    player = Player('Name', team)
    assert player.name == 'Name'
    assert player.team == team
    assert player.is_dealer is False
    assert len(player.hand) == 0
    assert player.trick_winner is False
    assert player.__repr__() == 'Player(Name, Team, False)'
    assert player.__str__() == 'Name'

    player.is_dealer = True
    assert player.__str__() == 'Name (Dealer)'
