
from . import Team, Card, Suit


class Player():
    """Representation of a player. Parent class of Computer and Human.
    """

    def __init__(self, name: str, team: Team) -> None:
        self.name = name
        self.team = team

        # reset every hand
        self.is_dealer = False
        self.hand = []

        # reset every trick
        self.trick_winner = False

    def won_trick(self) -> None:
        """Set trick_winner and team won trick.
        """
        self.trick_winner = True
        self.team.won_trick()

    def __repr__(self) -> str:
        return f"Player({self.name}, {self.team.name}, {self.is_dealer})"

    def __str__(self) -> str:
        if self.is_dealer:
            return f"{self.name} (Dealer)"
        else:
            return f"{self.name}"
