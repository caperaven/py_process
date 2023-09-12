from process_api.modules.selenium.get import get_element


async def wait(driver, args):
    timeout = args["timeout"] if "timeout" in args else 10

    if "query" in args:
        query = args["query"]
        element = await get_element(driver, query, timeout)
        return element
