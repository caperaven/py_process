from src.action_systems.selenium.driver import Driver
from src.action_systems.selenium.navigate import goto
from src.utils.get_value import get_value


async def get_driver(step, context=None, process=None, item=None):
    args = step["args"]
    return await get_value(args.get("driver"), context, process, item)


class Default:

    @staticmethod
    async def init_driver(step, context=None, process=None, item=None):
        args = step["args"]
        browser = await get_value(args.get("browser"), context, process, item)
        options = await get_value(args.get("options"), context, process, item)
        return await Driver.init(browser, options)

    @staticmethod
    async def close_driver(step, context=None, process=None, item=None):
        driver = await get_driver(step, context, process, item)
        await Driver.close(driver)

    @staticmethod
    async def goto(step, context=None, process=None, item=None):
        args = step["args"]
        driver = await get_driver(step, context, process, item)
        url = await get_value(args.get("url"), context, process, item)
        await goto(driver, url)

    @staticmethod
    async def get(step, context=None, process=None, item=None):
        pass

    @staticmethod
    async def set(step, context=None, process=None, item=None):
        pass

    @staticmethod
    async def wait(step, context=None, process=None, item=None):
        pass
