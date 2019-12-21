from spyc.internal import build_spec
import itertools


class specification_type:
    pass


def specs(specs):
    return __specs(build_spec(specs))


class __specs(specification_type):
    def __init__(self, specs):
        self.__specs = specs

    def is_valid(self, target):
        return self.__specs.is_valid(target)


class type_spec(specification_type):
    def __init__(self, type):
        self.__type = type

    def is_valid(self, target):
        return isinstance(target, self.__type)


class callable_spec(specification_type):
    def __init__(self, callable):
        self.__callable = callable

    def is_valid(self, target):
        return self.__callable(target)


def either(*specs):
    return either_spec([build_spec(spec) for spec in specs])


class either_spec(specification_type):
    def __init__(self, specs):
        self.__specs = specs

    def is_valid(self, target):
        for spec in self.__specs:
            if spec.is_valid(target):
                return True
        return False


def all_of(*specs):
    return all_of_spec([build_spec(spec) for spec in specs])


class all_of_spec(specification_type):
    def __init__(self, specs):
        self.__specs = specs

    def is_valid(self, target):
        for spec in self.__specs:
            if not spec.is_valid(target):
                return False
        return True


class with_members(specification_type):
    def __init__(self, *members, **checked_members):
        self.__members = members
        self.__checked_members = {
            name: build_spec(spec)
            for name, spec in checked_members.items()
        }

    def is_valid(self, target):
        needed_members = itertools.chain(self.__members,
                                         self.__checked_members.keys())
        for member in needed_members:
            if not hasattr(target, member):
                return False

        for checked_member, spec in self.__checked_members.items():
            if not spec.is_valid(getattr(target, checked_member)):
                return False

        return True
