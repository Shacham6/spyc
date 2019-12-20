from specs.internal import conform_spec


class specification:
    pass


class type_spec(specification):
    def __init__(self, type):
        self.__type = type

    def is_valid(self, target):
        return isinstance(target, self.__type)


class callable_spec(specification):
    def __init__(self, callable):
        self.__callable = callable

    def is_valid(self, target):
        return self.__callable(target)


def either(*specs):
    return either_spec([conform_spec(spec) for spec in specs])


class either_spec(specification):
    def __init__(self, specs):
        self.__specs = specs

    def is_valid(self, target):
        for spec in self.__specs:
            if spec.is_valid(target):
                return True
        return False


def all_of(*specs):
    return all_of_spec([conform_spec(spec) for spec in specs])


class all_of_spec(specification):
    def __init__(self, specs):
        self.__specs = specs

    def is_valid(self, target):
        for spec in self.__specs:
            if not spec.is_valid(target):
                return False
        return True
