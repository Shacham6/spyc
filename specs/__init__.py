from specs import spec_types, internal
from specs.spec_types import either, all_of, specs, with_members


def is_valid(target, requirements):
    return specs(requirements).is_valid(target)
