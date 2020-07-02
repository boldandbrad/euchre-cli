
from euchrecli.card_util import Card, Suit
from euchrecli.player_util import Player

def valid_play(card_to_play: Card, played_cards: [Card], trump_suit: Suit) -> bool:
    # TODO: implement
    return True

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
