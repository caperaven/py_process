from src.action_systems.selenium.get import get_element


async def wait(driver, args):
    if "query" in args:
        query = args["query"]
        timeout = args["timeout"] if "timeout" in args else 10
        await get_element(driver, query, timeout)
    pass
