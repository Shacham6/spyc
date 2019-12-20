from specs import spec_types, internal
from specs.spec_types import either


def is_valid(target, specs):
    specs = internal.conform_spec(specs)
    return specs.is_valid(target)
