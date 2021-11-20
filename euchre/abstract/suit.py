
class Suit():
    """Representation of a standard playing card suit.
    """

    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def __repr__(self) -> str:
        return f"Suit({self.name}, {self.color})"

    def __str__(self) -> str:
        return f"{self.name}"
