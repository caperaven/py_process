from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


async def get(driver, args):
    query = args.get("element")
    timeout = args.get("timeout", 10)
    context = args.get("context", driver)
    element = await get_element(context, query, timeout)

    if "attribute" in args:
        attribute = args["attribute"]
        return element.get_attribute(attribute)

    if "property" in args:
        return element.get_property(args["property"])

    return element


async def get_element(context, query, timeout):
    if isinstance(query, WebElement):
        return query

    wait = WebDriverWait(context, timeout, poll_frequency=0.1)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, query)))
    return element
