
from . import Suit, Face


class Card():
    """Representation of a standard playing card.
    """

    def __init__(self, suit: Suit, face: Face) -> None:
        self.suit = suit
        self.face = face

    def is_left_bower(self, trump_suit: Suit) -> bool:
        """Check if this card is the left bower.

        Args:
            trump_suit (Suit): Active trump suit.

        Returns:
            bool: Whether the card is the left bower.
        """
        # if jack of same color as trump suit
        return self.face.name == 'Jack' and \
            self.suit.color == trump_suit.color and \
            self.suit.name != trump_suit.name

    def adjusted_suit(self, trump_suit: Suit) -> Suit:
        """Return trump suit if card is left bower.

        Args:
            trump_suit (Suit): Active trump suit.

        Returns:
            Suit: Card adjusted suit.
        """
        if self.is_left_bower(trump_suit):
            return trump_suit
        else:
            return self.suit

    def weighted_value(self, trump_suit: Suit, lead_suit: Suit = None) -> int:
        """Calculate card weighted value relative to trump and/or lead suits.

        When lead == trump:
            trump:  9(21), 10(22), Q(23), K(24), A(25), Left(26), Right(27)
            else:   9(9), 10(10), J(11), Q(12), K(13), A(14)

        When lead != trump:
            trump:  9(21), 10(22), Q(23), K(24), A(25), Left(26), Right(27)
            lead:   9(15), 10(16), J(17), Q(18), K(19), A(20)
            else:   9(9), 10(10), J(11), Q(12), K(13), A(14)

        Args:
            trump_suit (Suit): Active trump suit.
            lead_suit (Suit): Active lead suit.

        Returns:
            int: Card weighted value.
        """
        weighted_val = self.face.value  # 9, 10, 11, 12, 13, 14

        if self.is_left_bower(trump_suit):
            weighted_val += 15  # 26
        elif self.suit.name == trump_suit.name:
            if self.face.name in ['Nine', 'Ten']:
                weighted_val += 12  # 21, 22
            elif self.face.name in ['Queen', 'King', 'Ace']:
                weighted_val += 11  # 23, 24, 25
            elif self.face.name == 'Jack':
                weighted_val += 16  # 27 (right_bower)
        elif lead_suit and trump_suit.name != lead_suit.name and \
                self.suit.name == lead_suit.name:
            weighted_val += 6  # 15, 16, 17, 18, 19, 20

        return weighted_val

    def __repr__(self) -> str:
        return f"Card({self.face.name}, {self.suit.name})"

    def __str__(self) -> str:
        return f"{self.face.name} of {self.suit.name}s"
