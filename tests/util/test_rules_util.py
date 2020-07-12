
from euchrecli.abstract import Face, Suit, Card, Team, Computer
from euchrecli.util.rule_util import valid_play, hand_winner, trick_winner


def test_valid_play():
    """Test rule_util.valid_play()
    """
    spades = Suit('Spade', 'Black')
    diamonds = Suit('Diamond', 'Red')

    trump_suit = spades

    player_hand = [
        Card(spades, Face('Jack', 11)),
        Card(diamonds, Face('Nine', 9))
    ]

    # no cards yet played
    played_cards = []

    card_to_play = player_hand[0]
    assert valid_play(card_to_play, player_hand, played_cards, trump_suit) \
        is True

    # lead card played
    played_cards = [
        Card(diamonds, Face('Ten', 10))
    ]

    # did not follow suit
    card_to_play = player_hand[0]  # Jack of Spades
    assert valid_play(card_to_play, player_hand, played_cards, trump_suit) \
        is False

    # followed suit
    card_to_play = player_hand[1]  # Nine of Diamonds
    assert valid_play(card_to_play, player_hand, played_cards, trump_suit) \
        is True


def test_trick_winner():
    """Test rule_util.trick_winner()
    """
    t1 = Team('t1')
    t2 = Team('t2')

    players = [
        Computer('p1', t1),
        Computer('p2', t2),
        Computer('p3', t1),
        Computer('p4', t2)
    ]

    spades = Suit('Spade', 'Black')
    clubs = Suit('Club', 'Black')
    diamonds = Suit('Diamond', 'Red')

    trump_suit = spades

    played_cards = [
        Card(diamonds, Face('Ten', 10)),
        Card(spades, Face('Ace', 14)),
        Card(diamonds, Face('Nine', 9)),
        Card(clubs, Face('Jack', 11))
    ]
    assert trick_winner(players, played_cards, trump_suit) == players[3]


def test_hand_winner():
    """Test rule_util.hand_winner()
    """
    # team called trump and took 3/4 tricks
    teams = [Team('t1'), Team('t2')]
    teams[0].trick_score = 3
    teams[0].called_trump = True
    teams[1].trick_score = 2
    assert hand_winner(teams) == teams[0] and teams[0].game_score == 1

    # team called trump and took all 5 tricks
    teams = [Team('t1'), Team('t2')]
    teams[0].trick_score = 5
    teams[0].called_trump = True
    teams[1].trick_score = 0
    assert hand_winner(teams) == teams[0] and teams[0].game_score == 2

    # team did not call trump and took 3 or more tricks
    teams = [Team('t1'), Team('t2')]
    teams[0].trick_score = 3
    teams[1].trick_score = 0
    teams[1].called_trump = True
    assert hand_winner(teams) == teams[0] and teams[0].game_score == 2

    # check that team trick scores are reset
    for team in teams:
        assert team.called_trump is False
        assert team.trick_score == 0
