
class Team():
    """Representation of a team of players.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.game_score = 0

        # reset every hand
        self.called_trump = False
        self.trick_score = 0

    def won_hand(self, points: int) -> None:
        """Increment game_score for winning hand.

        Args:
            points (int): Number of points to add to score.
        """
        self.game_score += points

    def won_trick(self) -> None:
        """Increment trick_score for winning trick.
        """
        self.trick_score += 1

    def __repr__(self) -> str:
        return f"Team({self.name})"

    def __str__(self) -> str:
        return f"{self.name}"
