
import click

from euchrecli.util.card_util import Card, Suit
from euchrecli.util.deck_util import create_deck, deal_hand
from euchrecli.util.player_util import Team, Player
from euchrecli.util.rule_util import valid_play, trick_winner, hand_winner


@click.command(help='Start a new euchre game.')
def play():
    setup()


def setup():
    """Setup players."""
    # TODO: implement setup from user input

    # TODO: implement random team assignment and order
    teams = [
        Team('Team 1'),
        Team('Team 2')
    ]
    players = [
        Player('Mitch', teams[0]),
        Player('Lena', teams[1]),
        Player('Bradley', teams[0]),
        Player('Morgan', teams[1])
    ]
    players[-1].is_dealer = True

    # start game
    game(players, teams)


def game(players: [Player], teams: [Team]):
    """Start game and manage team scores."""
    # play hands until the game is won
    game_won = False
    hand_number = 1
    while(not game_won):
        # deal and play hand
        hand(hand_number, players)

        # determine hand winner
        winning_team = hand_winner(teams)

        for team in teams:
            print(f'{team.name}: {team.game_score}')

        # check if winning team has won the game
        if winning_team.game_score >= 10:
            game_won = True
            print(f'{winning_team} wins!')

        hand_number += 1

        # TODO: implement dealer rotation
        players = rotate_dealer(players)
        print(f'New Dealer: {players}')

    # TODO: implement play again logic


def rotate_dealer(players: [Player]) -> [Player]:
    # rotate actual list for hands. use copy for tricks? find a way to manage
    # player scores and winners using copy
    players[-1].is_dealer = False
    players = players[1:] + players[:1]
    players[-1].is_dealer = True
    return players


def hand(number: int, players: [Player]) -> None:
    """Deal and play a hand."""
    print(f'\nPlay Hand {number}\n')
    trump_suit = None

    while not trump_suit:
        deck = create_deck()
        deal_hand(players, deck)

        for player in players:
            print(f'{player.name}\'s hand: {player.hand}')
        print(f'Deck: {deck}')

        trump_suit = set_trump_suit(players, deck)

        for player in players:
            print(f'{player.name} hand {player.hand}')
        print(f'Deck: {deck}')

    print(f'Trump suit is {trump_suit}')

    for _ in range(5):
        played_cards = trick(players, trump_suit)
        winning_player = trick_winner(players, played_cards, trump_suit)
        print(f'Trick winner {winning_player.name}, {winning_player.team}')

        for player in players:
            print(f'{player.name}\'s hand: {player.hand}')

        # TODO: adjust play order based on winner of previous trick


def set_trump_suit(players: [Player], deck: [Card]) -> Suit:
    """Set trump suit for the current hand."""
    print('Set trump suit')
    # dealer flips card
    face_up_card = deck[0]
    deck.pop(0)

    face_up_suit = face_up_card.suit

    print(f'Face up card is {face_up_card}')

    trump_suit = None

    # pickup round
    for player in players:
        if not trump_suit:
            if player.call_pick_up(face_up_card):
                print(f'{player.name} says pick it up')
                # capture trump suit and team that called for it
                trump_suit = face_up_card.suit
                player.team.called_trump = True

                # dealer picks up face up card
                replaced_card = players[3].pick_up_card(face_up_card)
                deck.append(replaced_card)
            else:
                print(f'{player.name} passes')

    # call round
    if not trump_suit:
        print(f'Trump suit cannot be {face_up_suit}')
        for player in players:
            if not trump_suit:
                candidate_suit = player.call_trump_suit(face_up_suit)
                print(f'{player.name} proposes {candidate_suit}')
                if candidate_suit != face_up_suit:
                    trump_suit = candidate_suit
                    player.team.called_trump = True
                else:
                    print(f'{player.name} passes')

    return trump_suit


def trick(players: [Player], trump_suit: Suit) -> [Card]:
    """Players take turns playing cards in a trick."""
    print('\nPlay Trick\n')
    played_cards = []
    for player in players:
        print(f'{player.name}')
        card_to_play = player.play_card(played_cards, trump_suit)
        while not valid_play(card_to_play, player.hand, played_cards,
                             trump_suit):
            card_to_play = player.play_card(played_cards, trump_suit)

        played_cards.append(card_to_play)
        player.remove_card(card_to_play)

    print(f'Played cards: {played_cards}')
    return(played_cards)
