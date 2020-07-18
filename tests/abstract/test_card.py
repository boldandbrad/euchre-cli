
from euchrecli.abstract import Face, Suit, Card


def test_card():
    suit = Suit('Spade', 'Black')
    face = Face('Ace', 14)
    card = Card(suit, face)
    assert card.suit == suit
    assert card.face == face
    assert card.__repr__() == 'Card(Ace, Spade)'
    assert card.__str__() == 'Ace of Spades'


def test_left_bower():
    suit = Suit('Spade', 'Black')
    face = Face('Jack', 11)
    card = Card(suit, face)

    trump_suit = Suit('Club', 'Black')
    assert card.is_left_bower(trump_suit) is True
    assert card.adjusted_suit(trump_suit) is trump_suit

    trump_suit = suit
    assert card.is_left_bower(trump_suit) is False
    assert card.adjusted_suit(trump_suit) is card.suit


def test_weighted_value():
    suit = Suit('Spade', 'Black')
    face = Face('Nine', 9)
    card = Card(suit, face)

    trump_suit = suit
    lead_suit = trump_suit

    assert card.weighted_value(trump_suit, lead_suit) == 21

    face = Face('Jack', 11)
    card = Card(suit, face)
    assert card.weighted_value(trump_suit, lead_suit) == 27
