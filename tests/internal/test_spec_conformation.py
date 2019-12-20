import pytest
from specs.internal import conform_spec, UnsupportedSpecification
from specs import is_valid, spec_types


@pytest.mark.parametrize("input, expected_type", [
    (int, spec_types.type_spec),
    (lambda *args: True, spec_types.callable_spec),
    (spec_types.either(int, float), spec_types.either_spec),
    (spec_types.all_of(int), spec_types.all_of_spec),
])
def test_conforms_types(input, expected_type):
    assert isinstance(conform_spec(input), expected_type)


def test_raises_when_provided_unsupported_spec():
    with pytest.raises(UnsupportedSpecification):
        conform_spec(22)
