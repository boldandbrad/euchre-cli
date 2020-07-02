
from euchrecli.card_util import Card, Suit
from euchrecli.player_util import Player


def valid_play(card_to_play: Card, player_hand: [Card], played_cards: [Card],
               trump_suit: Suit) -> bool:
    valid = False
    if len(played_cards) == 0 or len(player_hand) == 1:
        valid = True
        print(f'valid (1) {valid}')
    else:
        lead_suit = played_cards[0].adjusted_suit(trump_suit)
        if card_to_play.adjusted_suit(trump_suit) == lead_suit:
            valid = True
            print(f'valid (2) {valid}')
        else:
            lead_matches = 0
            for card in player_hand:
                if card != card_to_play and card.adjusted_suit(trump_suit) == \
                        lead_suit:
                    lead_matches += 1

            valid = lead_matches == 0  # TODO: change this to 'lead_matches == 0'
            print(f'valid (3) {lead_matches == 0}')

    return valid


def trick_winner(players: [Player], played_cards: [Card], trump_suit: Suit):
    """
    determine winner of trick by trump and lead weighted card values
    """
    lead_suit = played_cards[0].suit

    high_value = 0
    winning_player = None
    for idx, card in enumerate(played_cards):
        weighted_value = card.weighted_value(trump_suit, lead_suit)
        if weighted_value > high_value:
            high_value = weighted_value
            winning_player = players[idx]

    return winning_player


def score_hand(team_called: int):
    # TODO: implement
    pass
