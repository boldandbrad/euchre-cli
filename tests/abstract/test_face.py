
from euchrecli.abstract import Face


def test_face():
    face = Face('Ace', 14)
    assert face.name == 'Ace'
    assert face.value == 14
    assert face.__repr__() == 'Face(Ace, 14)'
    assert face.__str__() == 'Ace'
