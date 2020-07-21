
from random import shuffle

from euchrecli.abstract import Player, Suit, Face, Card


def create_deck() -> [Card]:
    """Return a shuffled standard euchre deck.

    Creates a deck containing 9, 10, J, Q, K, A of each suit.

    Returns:
        [Card]: Shuffled list of cards.
    """

    suits = [
        Suit('Spade', 'Black'),
        Suit('Club', 'Black'),
        Suit('Diamond', 'Red'),
        Suit('Heart', 'Red')
    ]
    faces = [
        Face('Nine', 9),
        Face('Ten', 10),
        Face('Jack', 11),
        Face('Queen', 12),
        Face('King', 13),
        Face('Ace', 14)
    ]

    deck = []
    for suit in suits:
        for face in faces:
            card = Card(suit, face)
            deck.append(card)

    shuffle(deck)
    return deck


def deal_hand(players: [Player], deck: [Card]) -> None:
    """Deal five cards from the deck to each player.

    Args:
        players ([Player]): Players to deal cards to.
        deck ([Card]): Deck to deal cards from.
    """
    # TODO: implement standard euchre dealing algorithm
    index = 0
    for player in players:
        player.hand = []
        for _ in range(5):
            player.hand.append(deck.pop(index))
