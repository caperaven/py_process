from src.utils.prefixes import CONTEXT_PREFIX, PROCESS_PARAMETERS_PREFIX, PROCESS_DATA_PREFIX, ITEM_PREFIX


async def get_value(value, context=None, process=None, item=None):
    if value is None:
        return None

    if value == "$c":
        return context

    if value == "$p":
        return get_property_on_path(process, ["parameters"])

    if value == "$d":
        return get_property_on_path(process, ["data"])

    if value == "$i":
        return item

    # if the value starts with $c{, then it is a context variable
    if value.startswith(CONTEXT_PREFIX) and context is not None:
        return get_property_on_path(context, value[3:-1].split("."))

    # if the value starts with $p{, then it is a process parameters variable
    if value.startswith(PROCESS_PARAMETERS_PREFIX) and process is not None and hasattr(process, "parameters"):
        return get_property_on_path(process.parameters, value[3:-1].split("."))

    # if the value starts with $d{, then it is a process data variable
    if value.startswith(PROCESS_DATA_PREFIX) and process is not None and hasattr(process, "data"):
        return get_property_on_path(process.data, value[3:-1].split("."))

    # if the value starts with $i{, then it is an item variable
    if value.startswith(ITEM_PREFIX) and item is not None:
        return get_property_on_path(item, value[3:-1].split("."))

    return value


# get_property_on_path is a recursive function that will get the value of a property on a path
# The path is split before calling this function to ensure better performance
# Example: get_property_on_path({"a": {"b": {"c": "d"}}}, ["a", "b", "c"]) will return "d"
def get_property_on_path(obj, path):
    if obj is None or path is None or len(path) == 0:
        return None

    result = None
    if isinstance(obj, dict):
        result = obj.get(path[0])

    if hasattr(obj, path[0]):
        result = getattr(obj, path[0])

    if len(path) == 1:
        return result

    return get_property_on_path(result, path[1:])
