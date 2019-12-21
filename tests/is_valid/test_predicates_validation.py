from spec import is_valid


def test_validated_by_result_of_callable():
    def is_even(item):
        return item % 2 == 0

    assert is_valid(2, is_even)
    assert not is_valid(1, is_even)
