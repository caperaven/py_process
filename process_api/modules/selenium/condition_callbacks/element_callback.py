from selenium.webdriver.common.by import By


def element_callback(element, args):
    def _predicate(driver):
        found_element = driver.find_element(By.CSS_SELECTOR, args["query"])
        present = args.get("present", True)

        if present and found_element is None:
            return False

        if not present and found_element is not None:
            return False

        return True

    return _predicate

