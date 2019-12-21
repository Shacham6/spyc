from spec import is_valid, either, all_of


def test_all_of_requires_everything_is_validated():
    def is_even(target):
        return target % 2 == 0

    even_integer = all_of(int, is_even)

    assert not is_valid(1, even_integer)
    assert not is_valid(2.0, even_integer)

    assert is_valid(2, even_integer)


def test_either_requires_at_least_on_item_to_be_validated():
    def is_even(target):
        return target % 2 == 0

    def is_odd(target):
        return target % 2 == 1

    even_or_odd_number = either(is_even, is_odd)
    assert is_valid(2, even_or_odd_number)
    assert is_valid(1, even_or_odd_number)
    assert not is_valid(2.3, even_or_odd_number)


def test_either_and_all_of_nest():
    def is_even(target):
        return target % 2 == 0

    def is_odd(target):
        return target % 2 == 1

    even_or_odd_integer = all_of(int, either(is_even, is_odd))
    assert is_valid(2, even_or_odd_integer)
    assert is_valid(1, even_or_odd_integer)
    assert not is_valid(2.5, even_or_odd_integer)
    assert not is_valid(2.0, even_or_odd_integer)
