
from euchrecli.util.card_util import Card, Suit
from euchrecli.util.player_util import Player, Team


def valid_play(card_to_play: Card, player_hand: [Card], played_cards: [Card],
               trump_suit: Suit) -> bool:
    """Return whether a card is a valid play."""
    valid = False
    if len(played_cards) == 0 or len(player_hand) == 1:
        valid = True
        print(f'{card_to_play}, ' +
              f'left: {card_to_play.is_left_bower(trump_suit)}, ' +
              f'valid (1): {valid}')
    else:
        lead_suit = played_cards[0].adjusted_suit(trump_suit)
        if card_to_play.adjusted_suit(trump_suit) == lead_suit:
            valid = True
            print(f'{card_to_play}, ' +
                  f'left: {card_to_play.is_left_bower(trump_suit)}, ' +
                  f'valid (2): {valid}')
        else:
            lead_matches = 0
            for card in player_hand:
                if card != card_to_play and card.adjusted_suit(trump_suit) == \
                        lead_suit:
                    lead_matches += 1

            valid = lead_matches == 0
            print(f'{card_to_play}, ' +
                  f'left: {card_to_play.is_left_bower(trump_suit)}, ' +
                  f'valid (3): {valid}')

    return valid


def trick_winner(players: [Player], played_cards: [Card], trump_suit: Suit):
    """Return winning player of trick. Increment their team's trick score."""
    lead_suit = played_cards[0].suit

    high_value = 0
    winning_player = None
    for idx, card in enumerate(played_cards):
        weighted_value = card.weighted_value(trump_suit, lead_suit)
        if weighted_value > high_value:
            high_value = weighted_value
            winning_player = players[idx]

    # increment team tricks won
    winning_player.won_trick()
    print(f'Trick winner {winning_player.name}, {winning_player.team}')


def hand_winner(teams: [Team]) -> Team:
    """Return winning team of the last hand. Increment team game_score."""
    winning_team = None
    for team in teams:
        if team.trick_score >= 3:
            winning_team = team
            # called trump and took 3 or 4 tricks
            if team.called_trump and team.trick_score in [3, 4]:
                team.won_hand(1)
            # called trump and took all 5 tricks
            elif team.called_trump and team.trick_score == 5:
                team.won_hand(2)
            # did not call trump but still took 3 or more tricks
            else:
                team.won_hand(2)

        # reset called_trump and trick_score
        team.called_trump = False
        team.trick_score = 0

    return winning_team
