class CallableSpec:
    def __init__(self, is_validated):
        self.__is_validated = is_validated

    def __match_specs__(self, target):
        return self.__is_validated(target)
