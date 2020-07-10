
import click
import names

from euchrecli.abstract import Team, Player, Computer, Human
from euchrecli.util.card_util import Card, Suit
from euchrecli.util.deck_util import create_deck, deal_hand
from euchrecli.util.player_util import set_dealer, rotate_dealer, \
    rotate_trick_order
from euchrecli.util.rule_util import valid_play, trick_winner, hand_winner


@click.command(
    help='Start a new euchre game.'
)
@click.option(
    '--watch',
    default=False,
    is_flag=True,
    help='Watch computers play a game of euchre amongst themselves.'
)
def play(watch):
    setup(watch)


def setup(watch_mode: bool):
    """Setup players and teams."""
    print(f'Welcome to euchre!')
    teams = [
        Team('Team 1'),
        Team('Team 2')
    ]

    if watch_mode:
        player = Computer(names.get_first_name(), teams[0])
    else:
        player = Human(teams[0])

    players = [
        player,
        Computer(names.get_first_name(), teams[1]),
        Computer(names.get_first_name(), teams[0]),
        Computer(names.get_first_name(), teams[1])
    ]

    deck = create_deck()
    set_dealer(players, deck)

    # start game
    game(players, teams)


def game(players: [Player], teams: [Team]):
    """Start game and manage team scores."""
    # play hands until the game is won
    game_won = False
    hand_number = 1
    while not game_won:
        # deal and play hand
        hand(hand_number, players)

        # determine hand winner
        winning_team = hand_winner(teams)

        print('Game Score')
        for team in teams:
            print(f'\t{team.name}: {team.game_score}')

        # check if winning team has won the game
        if winning_team.game_score >= 10:
            game_won = True
            print(f'{winning_team} wins!')
        else:
            # increment hand number
            hand_number += 1

            # rotate dealer to the left
            rotate_dealer(players)
            print(f'New Dealer: {players[-1].name}')

    # TODO: implement play again logic


def hand(number: int, players: [Player]) -> None:
    """Deal and play a hand."""
    print(f'\nPlay Hand {number}\n')
    trump_suit = None

    # set trump suit
    while not trump_suit:
        # create and shuffle deck then deal new hand
        deck = create_deck()
        deal_hand(players, deck)

        # set trump suit
        trump_suit = set_trump_suit(players, deck)

        # TODO: remove next three lines
        # for player in players:
        #     print(f'[DEBUG] ' +
        #           f'{player.name}\'s hand: {[str(c) for c in player.hand]}')
        # print(f'[DEBUG] Deck: {deck}')

    print(f'Trump suit is {trump_suit}s')

    # play 5 tricks
    for _ in range(5):
        # play trick and determine winner
        played_cards = trick(players, trump_suit)
        trick_winner(players, played_cards, trump_suit)

        # TODO: remove next two lines
        # for player in players:
        #     print(f'[DEBUG] ' +
        #           f'{player.name}\'s hand: {[str(c) for c in player.hand]}')

        # adjust play order based on winner of previous trick
        rotate_trick_order(players)


def set_trump_suit(players: [Player], deck: [Card]) -> Suit:
    """Set trump suit for the current hand."""
    # dealer flips card from top of deck
    face_up_card = deck.pop(0)
    face_up_suit = face_up_card.suit
    print(f'Face up card is {face_up_card}')

    trump_suit = None

    # pickup round
    for idx, player in enumerate(players):
        if not trump_suit:
            # if player is second in list then their partner is the dealer
            partner_is_dealer = idx == 1
            if player.call_pick_up(face_up_card, partner_is_dealer):
                print(f'{player.name} says pick it up!')
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
        # add face up card back to the deck
        deck.append(face_up_card)
        face_up_card = None
        print(f'Trump suit cannot be {face_up_suit}s')
        for player in players:
            if not trump_suit:
                candidate_suit = player.call_trump_suit(face_up_suit)
                if candidate_suit != face_up_suit:
                    print(f'{player.name} proposes {candidate_suit}s')
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
        print(f'{player.name}\'s play')
        # player picks a card until it is valid
        while True:
            card_to_play = player.play_card(played_cards, trump_suit)
            if valid_play(card_to_play, player.hand, played_cards, trump_suit):
                break
            if isinstance(player, Human):
                print(f'\tInvalid play ({str(card_to_play)}). You must ' +
                      f'follow the lead suit ' +
                      f'({played_cards[0].adjusted_suit(trump_suit)}s).')

        # play proposed card from player hand
        print(f'\t{str(card_to_play)}')
        played_cards.append(player.hand.pop(player.hand.index(card_to_play)))

    return(played_cards)
