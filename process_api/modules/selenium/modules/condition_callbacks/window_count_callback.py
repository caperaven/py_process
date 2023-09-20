def window_count_callback(element, args):
    def _predicate(driver):
        count = args.get("count", 0)
        length = len(driver.window_handles)

        return count == length

    return _predicate

