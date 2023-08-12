def get_value(value, context, process, item):
    if value is None:
        return None

    return value


def get_property_on_path(obj, path):
    if obj is None:
        return None

    if path is None:
        return None

    if len(path) == 0:
        return None

    if len(path) == 1:
        return obj[path[0]]

    return get_property_on_path(obj[path[0]], path[1:])