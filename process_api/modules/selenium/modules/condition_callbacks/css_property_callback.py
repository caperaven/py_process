def css_property_callback(element, args):
    def _predicate(driver):
        prop = args['property']
        exp_value = args["value"]

        value = element.value_of_css_property(prop)
        return value == exp_value

    return _predicate


def rgb_to_hex(rgba_string):
    return "#%02x%02x%02x%02x" % tuple(map(int, rgba_string[5:-1].split(",")))