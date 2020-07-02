
class Suit():

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def __repr__(self) -> str:
        return f"Suit({self.name}, {self.color})"

    def __str__(self) -> str:
        return f"{self.name}"


class Face():

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"Face({self.name}, {self.value})"

    def __str__(self) -> str:
        return f"{self.name}"


class Card():

    def __init__(self, suit: Suit, face: Face):
        self.suit = suit
        self.face = face

    def is_left_bower(self, trump_suit: Suit) -> bool:
        # if jack of same color as trump suit
        return self.face.name == 'Jack' and \
                self.suit.color == trump_suit.color and \
                self.suit.name != trump_suit.name

    def adjusted_suit(self, trump_suit: Suit) -> Suit:
        if self.is_left_bower(trump_suit):
            return trump_suit
        else:
            return self.suit

    def weighted_value(self, trump_suit: Suit, lead_suit: Suit) -> int:
        """Determine card weights relative to trump and/or lead suit cards.
        When lead == trump:
            trump:      9(21), 10(22), Q(23), K(24), A(25), Left(26), Right(27)
            else:       9(9), 10(10), J(11), Q(12), K(13), A(14)

        When lead != trump:
            trump:      9(21), 10(22), Q(23), K(24), A(25), Left(26), Right(27)
            lead:       9(15), 10(16), J(17), Q(18), K(19), A(20)
            else:       9(9), 10(10), J(11), Q(12), K(13), A(14)
        """
        weighted_value = self.face.value  # 9, 10, 11, 12, 13, 14

        if self.is_left_bower:
            weighted_value += 15  # 26
        elif self.suit.name == trump_suit.name:
            if self.face.name in ['Nine', 'Ten']:
                weighted_value += 12  # 21, 22
            elif self.face.name in ['Queen', 'King', 'Ace']:
                weighted_value += 11  # 23, 24, 25
            elif self.face.name == 'Jack':
                weighted_value += 16  # 27 (right_bower)
        elif trump_suit.name != lead_suit.name and \
                self.suit.name == lead_suit.name:
            weighted_value += 6  # 15, 16, 17, 18, 19, 20

        return weighted_value

    def __repr__(self) -> str:
        return f"Card({self.face.name}, {self.suit.name})"

    def __str__(self) -> str:
        return f"{self.face.name} of {self.suit.name}s"
