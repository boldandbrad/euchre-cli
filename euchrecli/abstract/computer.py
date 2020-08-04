
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

    def play_card(self, played_cards: [Card], trump_suit: Suit) -> Card:
        """Choose which card to play from hand.

        Args:
            played_cards ([type]): List of already played cards.
            trump_suit (Suit): Active trump suit.

        Returns:
            Card: Card to play.
        """

        # no cards have been played
        if not played_cards:
            # play highest card in hand
            high_hand_idx = self.hand.index(max(
                self.hand,
                key=lambda c: c.weighted_value(trump_suit)
            ))
            return self.hand[high_hand_idx]

        # get lead suit
        lead_suit = played_cards[0].adjusted_suit(trump_suit)

        # find highest card played
        high_played_idx = played_cards.index(max(
            played_cards,
            key=lambda c: c.weighted_value(trump_suit, lead_suit)
        ))
        high_played_value = played_cards[high_played_idx].weighted_value(
            trump_suit, lead_suit)

        # find lead and trump cards in hand
        lead_indicies = []
        trump_indicies = []
        for idx, card in enumerate(self.hand):
            if card.adjusted_suit(trump_suit) == lead_suit:
                lead_indicies.append(idx)
            # find trump cards if trump suit was not led
            if trump_suit != lead_suit and \
                    card.adjusted_suit(trump_suit) == trump_suit:
                trump_indicies.append(idx)

        # if player has lead cards
        if lead_indicies:
            if len(lead_indicies) == 1:
                # play only lead suit card
                return self.hand[lead_indicies[0]]

            # determine highest and lowest lead card indicies in hand
            high_lead_idx, low_lead_idx = self._hand_high_and_low_idxs(
                lead_indicies,
                trump_suit
            )
            high_lead_value = self.hand[high_lead_idx].weighted_value(
                trump_suit,
                lead_suit
            )
            # play highest lead card if it beats all played cards
            if high_lead_value > high_played_value:
                return self.hand[high_lead_idx]
            # else play lowest lead card
            else:
                return self.hand[low_lead_idx]

        # find lowest card in hand
        low_hand_idx = self.hand.index(min(
            self.hand,
            key=lambda c: c.weighted_value(trump_suit, lead_suit)
        ))

        # if player has trump cards
        if trump_indicies:
            # determine highest trump card in hand
            high_trump_idx, _ = self._hand_high_and_low_idxs(
                trump_indicies,
                trump_suit
            )
            high_trump_value = self.hand[high_trump_idx].weighted_value(
                trump_suit,
                lead_suit
            )
            # play highest trump card if it beats all played cards
            if high_trump_value > high_played_value:  # Fix to compare values
                return self.hand[high_trump_idx]

        # play lowest card in hand
        return self.hand[low_hand_idx]

    def _hand_high_and_low_idxs(self, indicies: [int], trump_suit: Suit) -> \
            (int, int):
        high_index = indicies[0]
        low_index = indicies[0]
        for idx in indicies:
            weighted_value = self.hand[idx].weighted_value(trump_suit)
            high_value = self.hand[high_index].weighted_value(trump_suit)
            low_value = self.hand[low_index].weighted_value(trump_suit)
            if weighted_value > high_value:
                high_index = idx
            if weighted_value < low_value:
                low_index = idx

        return high_index, low_index
