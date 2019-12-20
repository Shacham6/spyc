from specs import spec_types


def conform_spec(spec):
    if isinstance(spec, type):
        return spec_types.type_spec(spec)
    elif isinstance(spec, spec_types.specification):
        return spec
    raise UnsupportedSpecification()


class UnsupportedSpecification(Exception):
    pass
