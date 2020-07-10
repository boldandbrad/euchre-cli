
class Face():
    """Representation of a standard playing card face.
    """

    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"Face({self.name}, {self.value})"

    def __str__(self) -> str:
        return f"{self.name}"
