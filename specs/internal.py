from specs import spec_types


def conform_spec(spec):
    if isinstance(spec, type):
        return spec_types.type_spec(spec)
    return spec
