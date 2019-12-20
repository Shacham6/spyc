from specs import spec_types


def build_spec(spec):
    if isinstance(spec, spec_types.specification):
        return spec
    elif isinstance(spec, type):
        return spec_types.type_spec(spec)
    elif callable(spec):
        return spec_types.callable_spec(spec)
    raise UnsupportedSpecification()


class UnsupportedSpecification(Exception):
    pass
