from specs import spec_types
from specs.spec_types import either


def is_valid(target, specs):
    if isinstance(specs, type):
        specs = spec_types.type_spec(specs)
    return specs.is_valid(target)
