from typing import List

import names

from euchre.abstract import Player


def unique_cpu_name(players: List[Player]) -> str:
    """Create a unique player name.

    Args:
        players ([type]): existing players

    Returns:
        str: unique player name
    """
    taken_names = list(p.name.lower() for p in players)

    while True:
        name = names.get_first_name()
        if name.lower() not in taken_names:
            break

    return name


def rotate_dealer(players: List[Player]) -> None:
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


def rotate_trick_order(players: List[Player]) -> None:
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
