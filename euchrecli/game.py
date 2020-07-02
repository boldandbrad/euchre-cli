from euchrecli.card_util import Card, Suit
from euchrecli.deck_util import create_deck, deal_hand
from euchrecli.player_util import Team, Player
from euchrecli.rule_util import valid_play, trick_winner, score_hand


def setup():
    """
    game setup
    """
    # TODO: implement setup from user input

    # TODO: implement random team assignment and order
    team_1 = Team('Team 1')
    team_2 = Team('Team 2')
    players = [
        Player('Mitch', team_1),
        Player('Lena', team_2),
        Player('Bradley', team_1),
        Player('Morgan', team_2)
    ]
    players[3].is_dealer = True

    game(players)


def game(players: [Player]):
    """
    start game and manage team scores
    """
    team_won = False

    hand_number = 1
    while(not team_won):
        team_called = hand(players)
        score_hand(team_called)
        team_won = True
        hand_number += 1
        # TODO: implement dealer rotation


def hand(players: [Player]) -> int:
    """
    deal and play a hand
    """
    print('play hand')
    trump_suit = None
    team_called = None

    while not trump_suit:
        deck = create_deck()
        deal_hand(players, deck)

        for player in players:
            print(f'{player.name} hand {player.hand}')
        print('deck', deck)

        trump_suit, team_called = set_trump_suit(players, deck)

        for player in players:
            print(f'{player.name} hand {player.hand}')
        print('deck', deck)

    print(f'trump is {trump_suit}')

    for _ in range(5):
        played_cards = trick(players, trump_suit)
        winner = trick_winner(players, played_cards, trump_suit)
        print(f'trick winner {winner.name}')
        winner.team.won_trick()

        for player in players:
            print(f'{player.name} hand {player.hand}')
        # TODO: adjust play order based on winner of previous trick

    return team_called  # and potentially number of tricks won for each team?


def set_trump_suit(players: [Player], deck: [Card]) -> (Suit, int):
    """
    set trump suit for the current hand
    """
    print('set trump')
    # dealer flips card
    face_up_card = deck[0]
    deck.pop(0)

    face_up_suit = face_up_card.suit

    print('face up is', face_up_card)

    trump_suit = None
    team_called = None

    # pickup round
    for player in players:
        if not trump_suit:
            if player.call_pick_up(face_up_card):
                print(f'{player.name} says pick it up')
                # capture trump suit and team that called for it
                trump_suit = face_up_card.suit
                team_called = player.team

                # dealer picks up face up card
                replaced_card = players[3].pick_up_card(face_up_card)
                deck.append(replaced_card)
            else:
                print(f'{player.name} passes')

    # call round
    if not trump_suit:
        print(f'trump suit cannot be {face_up_suit}')
        for player in players:
            if not trump_suit:
                candidate_suit = player.call_trump_suit(face_up_suit)
                print(f'{player.name} proposes {candidate_suit}')
                if candidate_suit != face_up_suit:
                    trump_suit = candidate_suit
                    team_called = player.team
                else:
                    print(f'{player.name} passes')

    return trump_suit, team_called


def trick(players: [Player], trump_suit: Suit) -> [Card]:
    print('play trick')
    played_cards = []
    for player in players:
        card_to_play = player.play_card(played_cards, trump_suit)
        while not valid_play(card_to_play, player.hand, played_cards,
                             trump_suit):
            card_to_play = player.play_card(played_cards, trump_suit)

        played_cards.append(card_to_play)
        player.remove_card(card_to_play)

    print(f'played cards {played_cards}')
    return(played_cards)
