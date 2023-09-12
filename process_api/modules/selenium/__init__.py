from process_api.modules.selenium.driver import Driver
from process_api.modules.selenium.navigate import goto
from process_api.modules.selenium.get import get
from process_api.modules.selenium.set import set
from process_api.modules.selenium.wait import wait
from process_api.modules.selenium.perform import perform
from process_api.utils.get_value import get_value


async def get_driver(step, context=None, process=None, item=None):
    args = step["args"]
    return await get_value(args.get("driver"), context, process, item)


class SeleniumModule:
    @staticmethod
    def register(api):
        api.add_module("selenium", SeleniumModule)

    @staticmethod
    async def init_driver(api, step, context=None, process=None, item=None):
        args = step["args"]
        browser = await get_value(args.get("browser"), context, process, item)
        options = await get_value(args.get("options"), context, process, item)
        return await Driver.init(browser, options)

    @staticmethod
    async def close_driver(api, step, context=None, process=None, item=None):
        driver = await get_driver(step, context, process, item)
        await Driver.close(driver)

    @staticmethod
    async def goto(api, step, context=None, process=None, item=None):
        args = step["args"]
        driver = await get_driver(step, context, process, item)
        url = await get_value(args.get("url"), context, process, item)
        await goto(driver, url)

    @staticmethod
    async def get(api, step, context=None, process=None, item=None):
        driver = await get_driver(step, context, process, item)
        return await get(driver, step["args"])

    @staticmethod
    async def set(api, step, context=None, process=None, item=None):
        driver = await get_driver(step, context, process, item)
        return await set(driver, step["args"])

    @staticmethod
    async def wait(api, step, context=None, process=None, item=None):
        driver = await get_driver(step, context, process, item)
        return await wait(driver, step["args"])

    @staticmethod
    async def perform(api, step, context=None, process=None, item=None):
        driver = await get_driver(step, context, process, item)
        return await perform(driver, step["args"])