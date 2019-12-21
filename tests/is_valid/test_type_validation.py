from spec import is_valid, either


class Person:
    pass


def test_is_valid_cuptures_types():
    assert is_valid(2, int)
    assert not is_valid(2, str)
    assert is_valid(Person(), Person)
    assert not is_valid(3, Person)
