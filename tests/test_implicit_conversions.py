from spec import specs


def _is_even(item):
    return isinstance(item, (int, float,)) \
        and item % 2 == 0


def test_specs_accepts_functions():
    even_number = specs(_is_even)
    assert not even_number(1)
    assert even_number(2)


def test_specs_accepts_concret_types():
    integer = specs(int)
    assert not integer(2.3)
    assert integer(2)
