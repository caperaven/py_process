def style_property_callback(element, args):
    def _predicate(driver):
        prop = args['property']
        exp_value = args["value"]

        value = element.value_of_css_property(prop)
        return value == exp_value

    return _predicate
