class ClassSpec:
    def __init__(self, spec_type):
        self.__spec_type = spec_type

    def __match_specs__(self, target):
        return isinstance(target, self.__spec_type)
