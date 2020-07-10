
from . import Team, Player, Card, Suit
from euchrecli.util.input_util import bool_input, int_input, str_input


class Human(Player):
    """Representation of a human player. Extends Player class.
    """

    def __init__(self, team: Team):
        name = str_input('What is your name?')
        super().__init__(name, team)

    def call_pick_up(self, face_up_card: Card, partner_is_dealer: bool) \
            -> bool:
        """Decide whether to call pick up of face up card or to pass.

        Returns:
            bool: whether or not to call pick up
        """
        self._print_hand()
        choice = False
        if self.is_dealer:
            choice = bool_input(f'Would you like to pick up the ' +
                                f'{str(face_up_card)}?')
        else:
            choice = bool_input(f'Would you like the dealer to pick up the ' +
                                f'{str(face_up_card)}?')
        return choice

    def call_trump_suit(self, unsuitable: Suit) -> Suit:
        """Decide whether to call desired trump suit or to pass.

        Args:
            unsuitable (Suit): Trump suit cannot be this suit

        Returns:
            Suit: Called trump suit or unsuitable to pass
        """
        self._print_hand()
        suits_in_hand = set()
        for c in self.hand:
            if c.suit != unsuitable:
                suits_in_hand.add(c.suit)
        suits_in_hand = list(suits_in_hand)
        suits_in_hand.append(unsuitable)

        print(f'Possible options:')
        for idx, suit in enumerate(suits_in_hand):
            if suit != unsuitable:
                print(f'\t{idx} - {str(suit)}')
            else:
                print(f'\t{idx} - Pass')

        choice = int_input(f'Would you like to call a trump suit?',
                           len(suits_in_hand))

        return suits_in_hand[choice]

    def pick_up_card(self, pick_up: Card) -> Card:
        """Choose whether or not to replace card in hand with picked up one.

        Args:
            pick_up (Card): Card to pick up.

        Returns:
            Card: Card to be discarded.
        """
        # add picked up card to hand
        self.hand.insert(0, pick_up)
        print(f'You picked up the {str(pick_up)}.')

        self._print_hand(indexes=True)
        print(f'Trump suit will be {pick_up.suit}s.')
        choice = int_input(f'Which card would you like to discard?',
                           len(self.hand))
        discard = self.hand.pop(choice)
        print(f'You discarded the {str(discard)} to the deck.')
        return discard

    def play_card(self, played_cards: [Card], trump_suit: Suit) -> Card:
        self._print_hand(indexes=True)
        choice = int_input(f'Which card would you like to play?',
                           len(self.hand))
        return self.hand[choice]

    def _print_hand(self, indexes: bool = False):
        print(f'Your hand:')
        for idx, card in enumerate(self.hand):
            if indexes:
                print(f'\t{idx} - {str(card)}')
            else:
                print(f'\t{str(card)}')
