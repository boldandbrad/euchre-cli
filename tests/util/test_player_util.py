
from euchrecli.abstract import Computer
from euchrecli.util.player_util import rotate_dealer, rotate_trick_order


def test_rotate_dealer():
    """Test player_util.rotate_dealer()
    """
    players = [
        Computer('p1', 't1'),
        Computer('p2', 't2'),
        Computer('p3', 't1'),
        Computer('p4', 't2')
    ]

    players[0].is_dealer = True
    rotate_dealer(players)

    assert players[2].name == 'p1'
    assert players[2].is_dealer is False
    assert players[3].name == 'p2'
    assert players[3].is_dealer is True


def test_rotate_trick_order():
    players = [
        Computer('p1', 't1'),
        Computer('p2', 't2'),
        Computer('p3', 't1'),
        Computer('p4', 't2')
    ]

    players[2].trick_winner = True

    rotate_trick_order(players)

    assert players[0].name == 'p3'
    assert players[1].name == 'p4'
    for player in players:
        assert player.trick_winner is False
