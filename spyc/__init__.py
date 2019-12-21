from spyc import spec_types, internal
from spyc.spec_types import either, all_of, specs, with_members


def is_valid(target, requirements):
    return specs(requirements).is_valid(target)


def ensure(target, requirements):
    if not specs(requirements).is_valid(target):
        raise TargetInvalidException()


class TargetInvalidException(Exception):
    pass
