def attributes_callback(element, args):
    def _predicate(driver):
        attributes = args["attributes"].keys()

        for attribute in attributes:
            exp_value = args["attributes"][attribute]
            value = element.get_attribute(attribute)

            if value != exp_value:
                return False

        return True
    return _predicate
