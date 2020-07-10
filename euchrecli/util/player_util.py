
from random import choice, choices

from euchrecli.util.card_util import Card, Suit


class Team():

    def __init__(self, name: str) -> None:
        self.name = name
        self.game_score = 0

        # reset every hand
        self.called_trump = False
        self.trick_score = 0

    def won_hand(self, points: int) -> None:
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

    def __init__(self, name: str, team: Team) -> None:
        self.name = name
        self.team = team

        # reset every hand
        self.is_dealer = False
        self.hand = []

        # reset every trick
        self.trick_winner = False

    def call_pick_up(self, face_up_card: Card, partner_is_dealer: bool) \
            -> bool:
        """Decide whether to call pick up of face up card or to pass.

        Returns:
            bool: whether or not to call pick up
        """
        # determine which cards in hand match face up card suit
        suit = face_up_card.suit
        cards_of_suit = [
            card for card in self.hand if card.adjusted_suit(suit) == suit
        ]

        # TODO: consider if player is 2, 3, or 4 suited

        if partner_is_dealer and len(cards_of_suit) >= 2:
            return True
        elif self.is_dealer and len(cards_of_suit) >= 3:
            return True
        elif len(cards_of_suit) >= 3 and face_up_card.face.name != 'Jack':
            return True
        else:
            # only occasionally call on 'accident'
            return choices([True, False], weights=[1, 10])[0]

    def call_trump_suit(self, unsuitable: Suit) -> Suit:
        """Decide whether to call desired trump suit or to pass.

        Args:
            unsuitable (Suit): Trump suit cannot be this suit

        Returns:
            Suit: Called trump suit or unsuitable to pass
        """
        # TODO: simplify method logic
        # find suitable suits in hand
        suits_in_hand = set()
        for c in self.hand:
            if c.suit != unsuitable:
                suits_in_hand.add(c.suit)

        # find how many of each potential trump suit in hand
        suit_counts = []
        for suit in suits_in_hand:
            count = len(list(filter(
                lambda card: card.adjusted_suit(suit) == suit, self.hand
            )))
            suit_counts.append({'suit': suit, 'count': count})

        # sort suits by highest count
        suit_counts = sorted(suit_counts, key=lambda k: k['count'],
                             reverse=True)

        # call trump suit if player would have 3 or more trump cards
        # TODO: take into account card weights
        # TODO: take into account the passed on face_up_card
        # TODO: consider if player is 2, 3, or 4 suited
        if suit_counts[0]['count'] >= 3:
            return suit_counts[0]['suit']
        else:
            return unsuitable

    def pick_up_card(self, pick_up: Card) -> Card:
        """Choose whether or not to replace card in hand with picked up one.

        Args:
            pick_up (Card): Card to pick up.

        Returns:
            Card: Card to be discarded.
        """
        # add picked up card to hand
        self.hand.insert(0, pick_up)

        trump = lead = pick_up.suit

        # find lowest valued card in hand
        low_index = 0
        for idx, card in enumerate(self.hand):
            # TODO: consider if player is 2, 3, or 4 suited
            card_val = card.weighted_value(trump, lead)
            low_val = self.hand[low_index].weighted_value(trump, lead)
            if card_val < low_val:
                low_index = idx

        # return lowest valued card from hand
        return self.hand.pop(low_index)

    def play_card(self, played_cards: [Card], trump_suit: Suit) -> Card:
        # TODO: implement
        card_to_play = choice(self.hand)
        return card_to_play

    def won_trick(self) -> None:
        self.trick_winner = True
        self.team.won_trick()

    def __repr__(self) -> str:
        return f"Player({self.name}, {self.team}, {self.is_dealer})"

    def __str__(self) -> str:
        if self.is_dealer:
            return f"{self.name} - dealer"
        else:
            return f"{self.name}"


def set_dealer(players: [Player], deck: [Card]) -> None:
    """Set dealer by first dealt Black Jack.

    Args:
        players ([Player]): active game player list
        deck ([Card]): active deck of cards
    """
    print('First black jack deals!')
    dealer_set = False
    while not dealer_set:
        for player in players:
            card = deck.pop(0)
            print(f'\t{player.name}, {card}')
            if card.face.name == 'Jack' and card.suit.color == 'Black':
                player.is_dealer = True
                dealer_set = True
                print(f'{player.name} is dealer.')
                break

    # find dealer and rotate players so dealer is at the end of the list
    for idx, player in enumerate(players):
        if player.is_dealer:
            for _ in range(idx + 1):
                players.append(players.pop(0))

    print('Player Order:')
    for player in players:
        print(f'\t{str(player)}, {player.team.name}')


def rotate_dealer(players: [Player]) -> None:
    """Rotate the dealer to the left and update play order.

    Args:
        players ([Player]): active game player list
    """
    for idx, player in enumerate(players):
        if player.is_dealer:
            # rotate players based on index of previous dealer
            for _ in range(idx):
                players.append(players.pop(0))
            player.is_dealer = False

    # set new dealer
    players[-1].is_dealer = True


def rotate_trick_order(players: [Player]) -> None:
    """Rotate play order based on trick winner.

    Args:
        players ([Player]): active game player list
    """
    for idx, player in enumerate(players):
        if player.trick_winner:
            # rotate players based on index of previous trick winner
            for _ in range(idx):
                players.append(players.pop(0))
            player.trick_winner = False
