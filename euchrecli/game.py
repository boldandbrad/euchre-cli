from euchrecli.card_util import Card
from euchrecli.deck_util import create_deck, deal_hand
from euchrecli.player_util import Player


def setup():
    """
    game setup
    """
    players = [Player('Mitch'), Player('Lena'), Player('Bradley'), Player('Morgan')]
    players[3].is_dealer = True
    
    game(players)


def game(players: [Player]):
    """
    start game and manage team scores
    """
    team_won = False

    hand_number = 1
    while(not team_won):
        hand(players)
        team_won = True
        hand_number += 1


def hand(players: [Player]):
    """
    deal and play a hand
    """

    deck = create_deck()
    deal_hand(players, deck)

    # dealer flips card
    face_up_card = deck[0]
    deck.pop(0)

    trump_suit = None

    for player in players:
        print(player.hand)
    print(deck)
    print('face up', face_up_card)

    set_trump_suit()

    for _ in range(5):
        trick()


def set_trump_suit():
    """
    set trump suit for the current hand
    """
    pass


def trick():
    print('play trick')
