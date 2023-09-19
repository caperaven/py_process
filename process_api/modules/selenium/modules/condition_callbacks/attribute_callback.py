def attribute_callback(element, args):
    def _predicate(driver):
        value = element.get_attribute(args["attr"])
        exp_value = args["value"]
        return value == exp_value

    return _predicate
