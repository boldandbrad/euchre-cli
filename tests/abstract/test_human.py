
import pytest
from pytest_mock import mocker

from euchrecli.abstract import Human, Team, Face, Suit, Card


@pytest.fixture()
def human(mocker):
    mocker.patch('builtins.input', side_effect=['Name'])

    team = Team('Team')
    human = Human(team)

    return human


def test_human(human):
    assert human.name == 'Name'
    assert human.team.name == 'Team'
    assert human.is_dealer is False
    assert len(human.hand) == 0
    assert human.trick_winner is False
    assert human.__repr__() == 'Player(Name, Team, False)'
    assert human.__str__() == 'Name'

    human.is_dealer = True
    assert human.__str__() == 'Name (Dealer)'


def test_call_pick_up(mocker, human):
    mocker.patch('builtins.input', side_effect=['y', 'n'])

    # append card to hand
    suit = Suit('Spade', 'Black')
    face_9 = Face('Nine', 9)
    card = Card(suit, face_9)
    human.hand.append(card)

    # create face up card
    face_10 = Face('Ten', 10)
    face_up_card = Card(suit, face_10)

    # input is 'y'
    choice = human.call_pick_up(face_up_card, True)
    assert choice is True

    # input is 'n' and human is dealer
    human.is_dealer = True
    choice = human.call_pick_up(face_up_card, False)
    assert choice is False


def test_pick_up_card(mocker, human):
    mocker.patch('builtins.input', side_effect=[0])

    # append card to hand
    suit = Suit('Spade', 'Black')
    face_9 = Face('Nine', 9)
    card = Card(suit, face_9)
    human.hand.append(card)

    # create face up card
    face_10 = Face('Ten', 10)
    face_up_card = Card(suit, face_10)

    discard = human.pick_up_card(face_up_card)
    assert isinstance(discard, Card)
    assert discard not in human.hand


def test_call_trump_suit(mocker, human):
    mocker.patch('builtins.input', side_effect=[0])

    # append card to hand
    spades = Suit('Spade', 'Black')
    face_9 = Face('Nine', 9)
    card = Card(spades, face_9)
    human.hand.append(card)

    clubs = Suit('Club', 'Black')

    suit = human.call_trump_suit(clubs)
    assert isinstance(suit, Suit)
    assert suit in [spades, clubs]


def test_play_card(mocker, human):
    mocker.patch('builtins.input', side_effect=[0])

    # append card to hand
    spades = Suit('Spade', 'Black')
    face_9 = Face('Nine', 9)
    card = Card(spades, face_9)
    human.hand.append(card)

    played_cards = []
    card = human.play_card(played_cards, spades)
    assert isinstance(card, Card)
    assert card in human.hand
