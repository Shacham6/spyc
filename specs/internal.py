from specs import spec_types


def build_spec(requirements):
    if isinstance(requirements, spec_types.specification_type):
        return requirements
    elif isinstance(requirements, type):
        return spec_types.type_spec(requirements)
    elif callable(requirements):
        return spec_types.callable_spec(requirements)
    raise UnsupportedSpecification()


class UnsupportedSpecification(Exception):
    pass
