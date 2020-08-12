
from . import Team, Player, Card, Suit
from euchrecli.util import output
from euchrecli.util.input_util import bool_input, int_input, str_input


class Human(Player):
    """Representation of a human player. Extends Player class.
    """

    def __init__(self, team: Team):
        output(delay=0.75)
        name = str_input('What is your name?')
        super().__init__(name, team)

    def call_pick_up(self, face_up_card: Card, partner_is_dealer: bool) \
            -> bool:
        """Decide whether to call pick up of face up card or to pass.

        Returns:
            bool: whether or not to call pick up
        """
        self.print_hand()
        choice = False
        if self.is_dealer:
            choice = bool_input(f'Would you like to pick up the ' +
                                f'{str(face_up_card)}?')
        else:
            choice = bool_input(f'Would you like the dealer to pick up the ' +
                                f'{str(face_up_card)}?')
        return choice

    def pick_up_card(self, pick_up: Card) -> Card:
        """Choose whether or not to replace card in hand with picked up one.

        Args:
            pick_up (Card): Card to pick up.

        Returns:
            Card: Card to be discarded.
        """
        # add picked up card to hand
        self.hand.insert(0, pick_up)

        output(f'Trump suit will be {pick_up.suit}s.')
        self.print_hand(indicies=True)
        choice = int_input(f'Which card would you like to discard?',
                           len(self.hand))
        discard = self.hand.pop(choice)
        output(f'You discarded the {str(discard)} to the deck.', 0.75)
        return discard

    def call_trump_suit(self, unsuitable: Suit) -> Suit:
        """Decide whether to call desired trump suit or to pass.

        Args:
            unsuitable (Suit): Trump suit cannot be this suit

        Returns:
            Suit: Called trump suit or unsuitable to pass
        """
        self.print_hand()
        suits_in_hand = set()
        for c in self.hand:
            if c.suit != unsuitable:
                suits_in_hand.add(c.suit)
        suits_in_hand = list(suits_in_hand)
        suits_in_hand.append(unsuitable)

        output(f'Possible options:')
        for idx, suit in enumerate(suits_in_hand):
            if suit != unsuitable:
                output(f'\t{idx} - {str(suit)}', 0.75)
            else:
                output(f'\t{idx} - Pass', 0.75)

        choice = int_input(f'Would you like to call a trump suit?',
                           len(suits_in_hand))

        return suits_in_hand[choice]

    def play_card(self, played_cards: [Card], trump_suit: Suit) -> Card:
        """Choose which card to play from hand.

        Args:
            played_cards ([type]): List of already played cards.
            trump_suit (Suit): Active trump suit.

        Returns:
            Card: Card to play.
        """
        self.print_hand(indicies=True)
        choice = int_input(f'Which card would you like to play?',
                           len(self.hand))
        return self.hand[choice]

    def print_hand(self, indicies: bool = False):
        """Print out the player's hand.

        Args:
            indicies (bool, optional): Whether or not to include indicies.
                Defaults to False.
        """
        output(f'{self.name}, this is your hand:')
        for idx, card in enumerate(self.hand):
            if indicies:
                output(f'\t{idx} - {str(card)}', 0.75)
            else:
                output(f'\t{str(card)}', 0.75)
