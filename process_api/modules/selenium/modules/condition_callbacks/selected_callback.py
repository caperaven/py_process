def selected_callback(element, args):
    def _predicate(driver):
        exp_value = args.get("value", False)
        value = element.is_selected()

        return value == exp_value

    return _predicate
