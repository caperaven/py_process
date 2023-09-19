def element_properties_callback(element, args):
    def _predicate(driver):
        properties = args["properties"].keys()

        for prop in properties:
            exp_value = args["properties"][prop]
            value = element.get_property(prop)

            if value != exp_value:
                return False

        return True

    return _predicate
