
from euchrecli.card_util import Card, Suit

class Team():

    def __init__(self, name: str):
        self.name = name
        self.game_score = 0
        self.trick_score = 0

    def won_hand(self, points: int):
        self.game_score += points

    def won_trick(self):
        self.trick_score += 1

class Player():
    
    def __init__(self, name: str, team: Team):
        self.name = name
        self.team = team
        self.is_dealer = False
        self.hand = []

    def call_pick_up(self, face_up_card: Card) -> bool:
        # TODO: implement
        return False

    def call_trump_suit(self, unsuitable: Suit) -> Suit:
        # TODO: implement
        return list(filter(lambda card: card.suit != unsuitable , self.hand))[0].suit

    def pick_up_card(self, card: Card) -> Card:
        # TODO: implement
        replaced_card = self.hand[0]
        self.hand[0] = card
        return replaced_card
    
    def play_card(self, played_cards: [Card], trump_suit: Suit) -> Card:
        # TODO: implement
        return self.hand[0]

    def remove_card(self, card: Card):
        # TODO: implement
        self.hand.pop(self.hand.index(card))

    def __repr__(self) -> str:
        return f"Player({self.name}, {self.team}, {self.is_dealer})"
    
    def __str__(self) -> str:
        return f"{self.name}"

