def element_property_callback(element, args):
    def _predicate(driver):
        prop = args["property"]
        exp_value = args["value"]
        value = element.get_property(prop)

        return value == exp_value

    return _predicate
