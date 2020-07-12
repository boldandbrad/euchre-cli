
from euchrecli.abstract import Computer
from euchrecli.util import create_deck, deal_hand


def test_create_deck():
    """Test card_util.create_deck()
    """
    deck = create_deck()

    # check that deck is a standard euchre deck
    for card in deck:
        assert card.face.name in [
                'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'
            ]
        assert card.face.value >= 9 and card.face.value <= 14
        assert card.suit.name in [
                'Spade', 'Club', 'Diamond', 'Heart'
            ]
        assert card.suit.color in ['Black', 'Red']

    # check that there are no duplicate cards
    assert len(deck) == len(set(deck))


def test_deal_hand():
    """Test card_util.deal_hand()
    """
    players = [
        Computer('p1', 't1'),
        Computer('p2', 't2'),
        Computer('p3', 't1'),
        Computer('p4', 't2')
    ]
    deck = create_deck()

    deal_hand(players, deck)

    # check that all players have 5 cards in hand
    for player in players:
        assert len(player.hand) == 5

    # check that the deck now contains only 4 cards
    assert len(deck) == 4
