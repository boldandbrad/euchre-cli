
import click
import names
from loguru import logger

from euchrecli.abstract import Suit, Card, Team, Player, Computer, Human
from euchrecli.util import create_deck, deal_hand, output, rotate_dealer, \
    rotate_trick_order, valid_play, trick_winner, hand_winner


@click.command(
    help='Start a new euchre game.'
)
@click.help_option(
    '-h', '--help'
)
@click.option(
    '-w', '--watch',
    default=False,
    is_flag=True,
    help='Watch computers play a game of euchre amongst themselves.'
)
def play(watch: bool):
    setup(watch)


def setup(watch_mode: bool):
    """Setup players and teams."""
    output(f'Welcome to euchre-cli!', 0)

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

    output()
    output(f'Players:', 0.75)
    for player in players:
        output(f'\t{player.name}, {player.team.name}', 0.75)

    deck = create_deck()
    set_dealer(players, deck)

    # start game
    game(players, teams)


def set_dealer(players: [Player], deck: [Card]) -> None:
    """Set dealer by first dealt Black Jack.

    Args:
        players ([Player]): active game player list
        deck ([Card]): active deck of cards
    """
    output()
    output('First black jack deals:')
    dealer_set = False
    while not dealer_set:
        for player in players:
            card = deck.pop(0)
            output(f'\t{player.name}, {card}')
            if card.face.name == 'Jack' and card.suit.color == 'Black':
                player.is_dealer = True
                dealer_set = True
                output(f'{player.name} is the first dealer!')
                break

    # find dealer and rotate players so dealer is at the end of the list
    for idx, player in enumerate(players):
        if player.is_dealer:
            for _ in range(idx + 1):
                players.append(players.pop(0))


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

        output()
        output('Game Score:')
        for team in teams:
            output(f'\t{team.name}: {team.game_score}', 0.75)

        # check if winning team has won the game
        if winning_team.game_score >= 10:
            game_won = True
            output(f'{winning_team} wins!')
        else:
            # increment hand number
            hand_number += 1

            # rotate dealer to the left
            rotate_dealer(players)
            output(f'{players[-1].name} is the new dealer.')

    # TODO: implement play again logic


def hand(hand_num: int, players: [Player]) -> None:
    """Deal and play a hand."""
    output()
    output(f'Play Hand {hand_num}')
    output('---------------------------------------------')
    output()
    trump_suit = None

    # set trump suit
    while not trump_suit:
        # create and shuffle deck then deal new hand
        deck = create_deck()
        deal_hand(players, deck)
        output(f'{players[-1].name} has dealt the hand.')

        # set trump suit
        trump_suit = set_trump_suit(players, deck)

        if not trump_suit:
            output(
                f'Everyone has passed. {players[-1].name} will now re-deal.'
            )

        # log player hands and deck
        for player in players:
            logger.debug(
                f'{player.name}\'s hand: {[str(c) for c in player.hand]}'
            )
        logger.debug(f'Deck: {deck}')

    # play 5 tricks
    for trick_num in range(1, 6):
        # play trick and determine winner
        played_cards = trick(hand_num, trick_num, players, trump_suit)
        winning_player = trick_winner(players, played_cards, trump_suit)
        output(f'Trick winner: {winning_player.name}, {winning_player.team}')

        # log player hands
        for player in players:
            logger.debug(
                f'{player.name}\'s hand: {[str(c) for c in player.hand]}'
            )

        # adjust play order based on winner of previous trick
        rotate_trick_order(players)


def set_trump_suit(players: [Player], deck: [Card]) -> Suit:
    """Set trump suit for the current hand."""
    # dealer flips card from top of deck
    face_up_card = deck.pop(0)
    face_up_suit = face_up_card.suit
    output(f'The face up card is the {face_up_card}.')
    output()

    trump_suit = None

    # print human player's hand
    for player in players:
        if isinstance(player, Human):
            player.print_hand()
            output()

    # print play order for hand
    output('Play Order:')
    for player in players:
        output(f'\t{str(player)}, {player.team.name}', 0.75)
    output()

    # pickup round
    for idx, player in enumerate(players):
        if not trump_suit:
            # if player is second in list then their partner is the dealer
            partner_is_dealer = (idx == 1)
            if player.call_pick_up(face_up_card, partner_is_dealer):
                output(f'{player.name} says pick it up!')
                # capture trump suit and team that called for it
                trump_suit = face_up_card.suit
                player.team.called_trump = True

                # dealer picks up face up card and discards a card to the deck
                output(f'{players[-1].name} picked up the {face_up_card}.')
                replaced_card = players[-1].pick_up_card(face_up_card)
                deck.append(replaced_card)
            else:
                output(f'{player.name} passes.')

    # call round
    if not trump_suit:
        # add face up card back to the deck
        deck.append(face_up_card)
        face_up_card = None
        output()
        output(f'Trump suit cannot be {face_up_suit}s.')
        output()
        for player in players:
            if not trump_suit:
                candidate_suit = player.call_trump_suit(face_up_suit)
                if candidate_suit != face_up_suit:
                    output(f'{player.name} calls {candidate_suit}s.')
                    trump_suit = candidate_suit
                    player.team.called_trump = True
                else:
                    output(f'{player.name} passes.')

    return trump_suit


def trick(hand_num: int, trick_num: int, players: [Player], trump_suit: Suit) \
        -> [Card]:
    """Players take turns playing cards in a trick."""
    output()
    output(f'Hand {hand_num}, Trick {trick_num}')
    output()
    output(f'Trump suit is {trump_suit}s.')

    played_cards = []
    for player in players:
        # player picks a card until it is valid
        while True:
            card_to_play = player.play_card(played_cards, trump_suit)
            if valid_play(card_to_play, player.hand, played_cards, trump_suit):
                break
            if isinstance(player, Human):
                output(f'\tInvalid play ({str(card_to_play)}). You must ' +
                       f'follow the lead suit ' +
                       f'({played_cards[0].adjusted_suit(trump_suit)}s).', 0.5)
            else:
                logger.debug(f'\tInvalid play ({str(card_to_play)}).')

        # play proposed card from player hand
        output(f'{player.name} plays the')
        output(f'\t{card_to_play}', 0.75)
        played_cards.append(player.hand.pop(player.hand.index(card_to_play)))

    return played_cards
