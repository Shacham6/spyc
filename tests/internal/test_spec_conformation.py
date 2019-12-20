import pytest
from specs.internal import conform_spec, UnsupportedSpecification
from specs import is_valid, spec_types


def test_conforms_types():
    assert isinstance(
        conform_spec(int),
        spec_types.type_spec,
    )


def test_returns_self_when_spec_provided():
    assert isinstance(
        conform_spec(spec_types.either(int, str)),
        spec_types.either,
    )


def test_raises_when_provided_unsupported_spec():
    with pytest.raises(UnsupportedSpecification):
        conform_spec(22)
