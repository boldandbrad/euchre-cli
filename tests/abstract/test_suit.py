
from euchrecli.abstract import Suit


def test_suit():
    suit = Suit('Spade', 'Black')
    assert suit.name == 'Spade'
    assert suit.color == 'Black'
    assert suit.__repr__() == 'Suit(Spade, Black)'
    assert suit.__str__() == 'Spade'
