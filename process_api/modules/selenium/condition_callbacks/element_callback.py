from selenium.webdriver.common.by import By


def element_callback(element, args):
    def _predicate(driver):
        found_element = driver.find_element(By.CSS_SELECTOR, args["query"])
        present = args.get("present", True)

        if present and found_element is None:
            return False

        if not present and found_element is not None:
            return False

        return found_element

    return _predicate


def element_usable_callback(element):
    def _predicate(driver):
        if element is None:
            return False

        if element.is_enabled() and element.is_displayed():
            return element

    return _predicate


def light_and_shadow_dom_callback(element, shadow_root, query):
    def _predicate(driver):
        result_element = find_element(element, query)

        if result_element is not None:
            return result_element

        if shadow_root is not None:
            return find_element(shadow_root, query)

    return _predicate


def find_element(parent, query):
    try:
        return parent.find_element(By.CSS_SELECTOR, query)
    except:
        return None
