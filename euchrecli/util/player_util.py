
from random import choice, choices

from euchrecli.abstract import Team, Player, Card


def set_dealer(players: [Player], deck: [Card]) -> None:
    """Set dealer by first dealt Black Jack.

    Args:
        players ([Player]): active game player list
        deck ([Card]): active deck of cards
    """
    print('First black jack deals!')
    dealer_set = False
    while not dealer_set:
        for player in players:
            card = deck.pop(0)
            print(f'\t{player.name}, {card}')
            if card.face.name == 'Jack' and card.suit.color == 'Black':
                player.is_dealer = True
                dealer_set = True
                print(f'{player.name} is dealer.')
                break

    # find dealer and rotate players so dealer is at the end of the list
    for idx, player in enumerate(players):
        if player.is_dealer:
            for _ in range(idx + 1):
                players.append(players.pop(0))

    print('Player Order:')
    for player in players:
        print(f'\t{str(player)}, {player.team.name}')


def rotate_dealer(players: [Player]) -> None:
    """Rotate the dealer to the left and update play order.

    Args:
        players ([Player]): active game player list
    """
    for idx, player in enumerate(players):
        if player.is_dealer:
            # rotate players based on index of previous dealer
            for _ in range(idx):
                players.append(players.pop(0))
            player.is_dealer = False

    # set new dealer
    players[-1].is_dealer = True


def rotate_trick_order(players: [Player]) -> None:
    """Rotate play order based on trick winner.

    Args:
        players ([Player]): active game player list
    """
    for idx, player in enumerate(players):
        if player.trick_winner:
            # rotate players based on index of previous trick winner
            for _ in range(idx):
                players.append(players.pop(0))
            player.trick_winner = False
