
from random import choice, choices

from . import Team, Player, Card, Suit


class Computer(Player):
    """Representation of a cpu player. Extends Player class.
    """

    def __init__(self, name: str, team: Team):
        super().__init__(name, team)

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
        """Choose which card to play from hand.

        Args:
            played_cards ([type]): List of already played cards.
            trump_suit (Suit): Active trump suit.

        Returns:
            Card: Card to play.
        """
        # TODO: implement better decision making
        card_to_play = choice(self.hand)
        return card_to_play
