from spec import spec_types


class specs:
    def __init__(self, *requirements):
        self.__requirements = [
            self.__conform_spec(req) for req in requirements
        ]

    def __conform_spec(self, requirement):
        if isinstance(requirement, type):
            return spec_types.ClassSpec(requirement)

        elif callable(requirement):
            return spec_types.CallableSpec(requirement)

        raise UnsupportedSpec()

    def __call__(self, target):
        for requirement in self.__requirements:
            match_specs = getattr(requirement, "__match_specs__")
            matched = match_specs(target)
            if not matched:
                return False

        return True


class UnsupportedSpec(Exception):
    pass
