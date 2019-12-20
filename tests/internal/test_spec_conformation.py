from specs.internal import conform_spec
from specs import is_valid, spec_types


def test_conforms_types():
    assert isinstance(
        conform_spec(int),
        spec_types.type_spec,
    )
    assert isinstance(
        conform_spec(spec_types.either(int, str)),
        spec_types.either,
    )
