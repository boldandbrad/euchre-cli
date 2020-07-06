
from random import choice

from euchrecli.util.card_util import Card, Suit


class Team():

    def __init__(self, name: str):
        self.name = name
        self.game_score = 0

        # reset every hand
        self.called_trump = False
        self.trick_score = 0

    def won_hand(self, points: int):
        """Increment game_score for winning hand."""
        self.game_score += points

    def won_trick(self) -> None:
        """Increment trick_score for winning trick."""
        self.trick_score += 1

    def __repr__(self) -> str:
        return f"Team({self.name})"

    def __str__(self) -> str:
        return f"{self.name}"


class Player():

    def __init__(self, name: str, team: Team):
        self.name = name
        self.team = team

        # reset every hand
        self.is_dealer = False
        self.hand = []

        # reset every trick
        self.trick_winner = False

    def call_pick_up(self, face_up_card: Card) -> bool:
        # TODO: implement
        return choice([True, False, False, False])

    def call_trump_suit(self, unsuitable: Suit) -> Suit:
        # TODO: implement
        return list(filter(lambda card: card.suit != unsuitable,
                    self.hand))[0].suit

    def pick_up_card(self, card: Card) -> Card:
        # TODO: implement
        replaced_card = self.hand[0]
        self.hand[0] = card
        return replaced_card

    def play_card(self, played_cards: [Card], trump_suit: Suit) -> Card:
        # TODO: implement
        card_to_play = choice(self.hand)
        return card_to_play

    def remove_card(self, card: Card) -> None:
        self.hand.pop(self.hand.index(card))

    def won_trick(self) -> None:
        self.trick_winner = True
        self.team.won_trick()

    def __repr__(self) -> str:
        return f"Player({self.name}, {self.team}, {self.is_dealer})"

    def __str__(self) -> str:
        if self.is_dealer:
            return f"{self.name}, dealer"
        else:
            return f"{self.name}"


def rotate_dealer(players: [Player]) -> None:
    # rotate dealer to the left and reset player order
    for idx, player in enumerate(players):
        if player.is_dealer:
            # rotate players based on index of current dealer
            for _ in range(idx):
                players.append(players.pop(0))
            player.is_dealer = False

    # set new dealer
    players[-1].is_dealer = True


def rotate_trick_order(players: [Player]) -> None:
    # adjust play order based on winner of previous trick
    for idx, player in enumerate(players):
        if player.trick_winner:
            # rotate players based on index of trick winner
            for _ in range(idx):
                players.append(players.pop(0))
            player.trick_winner = False
