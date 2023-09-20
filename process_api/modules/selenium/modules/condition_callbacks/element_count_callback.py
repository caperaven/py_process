from selenium.webdriver.common.by import By


def element_count_callback(element, args):
    def _predicate(driver):
        count = args.get("count", 0)
        query = args.get("query", "*")
        elements = driver.find_elements(By.CSS_SELECTOR, query)
        exp_count = len(elements)

        return count == exp_count

    return _predicate

