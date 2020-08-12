
import pytest

from euchrecli.abstract import Computer, Team, Face, Suit, Card


@pytest.fixture()
def computer():
    team = Team('Team')
    computer = Computer('Name', team)

    return computer


def test_computer(computer):
    assert computer.name == 'Name'
    assert computer.team.name == 'Team'
    assert computer.is_dealer is False
    assert len(computer.hand) == 0
    assert computer.trick_winner is False
    assert computer.__repr__() == 'Player(Name, Team, False)'
    assert computer.__str__() == 'Name'

    computer.is_dealer = True
    assert computer.__str__() == 'Name (Dealer)'


def test_call_pick_up(computer):
    # append card to hand
    suit = Suit('Spade', 'Black')
    face_9 = Face('Nine', 9)
    card = Card(suit, face_9)
    computer.hand.append(card)

    # create face up card
    face_10 = Face('Ten', 10)
    face_up_card = Card(suit, face_10)

    choice = computer.call_pick_up(face_up_card, True)
    assert isinstance(choice, bool)


def test_pick_up_card(computer):
    # append card to hand
    suit = Suit('Spade', 'Black')
    face_9 = Face('Nine', 9)
    card = Card(suit, face_9)
    computer.hand.append(card)

    # create face up card
    face_10 = Face('Ten', 10)
    face_up_card = Card(suit, face_10)

    discard = computer.pick_up_card(face_up_card)
    assert isinstance(discard, Card)
    assert discard not in computer.hand


def test_call_trump_suit(computer):
    # append card to hand
    spades = Suit('Spade', 'Black')
    face_9 = Face('Nine', 9)
    card = Card(spades, face_9)
    computer.hand.append(card)

    clubs = Suit('Club', 'Black')

    suit = computer.call_trump_suit(clubs)
    assert isinstance(suit, Suit)
    assert suit in [spades, clubs]


def test_play_card(computer):
    # append card to hand
    spades = Suit('Spade', 'Black')
    face_9 = Face('Nine', 9)
    card = Card(spades, face_9)
    computer.hand.append(card)

    played_cards = []
    card = computer.play_card(played_cards, spades)
    assert isinstance(card, Card)
    assert card in computer.hand
