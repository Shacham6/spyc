class type_spec:
    def __init__(self, type):
        self.__type = type

    def is_valid(self, target):
        return isinstance(target, self.__type)


class either:
    def __init__(self, *specs):
        self.__specs = specs

    def is_valid(self, target):
        for spec in self.__specs:
            if isinstance(target, spec):
                return True
        return False
