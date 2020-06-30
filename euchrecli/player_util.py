
class Player():
    
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.is_dealer = False

    def __repr__(self) -> str:
        return f"Player({self.name}, {self.is_dealer})"
    
    def __str__(self) -> str:
        return f"{self.name}"

