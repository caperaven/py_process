def css_property_callback(element, args):
    def _predicate(driver):
        prop = args['property']
        value = element.value_of_css_property(prop)
        exp_value = args["value"]
        return value == exp_value

    return _predicate
