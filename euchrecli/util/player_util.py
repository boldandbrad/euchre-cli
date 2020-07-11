
from random import choice, choices

from euchrecli.abstract import Player


def rotate_dealer(players: [Player]) -> None:
    """Rotate the dealer to the left and update play order.

    Args:
        players ([Player]): active game player list
    """
    for idx, player in enumerate(players):
        if player.is_dealer:
            # rotate players based on index of previous dealer
            for _ in range(idx + 2):
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
