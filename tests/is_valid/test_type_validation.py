from specs import is_valid, either


class Person:
    pass


def test_is_valid_cuptures_types():
    assert is_valid(2, int)
    assert not is_valid(2, str)
    assert is_valid(Person(), Person)
    assert not is_valid(3, Person)


def test_either_matches_at_least_one_target():
    str_or_int = either(str, int)
    assert is_valid(2, str_or_int)
    assert is_valid("asd", str_or_int)
    assert not is_valid(5.5, str_or_int)
