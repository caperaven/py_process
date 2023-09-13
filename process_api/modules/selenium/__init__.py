from process_api.modules.selenium.driver import Driver
from process_api.modules.selenium.navigate import goto
from process_api.modules.selenium.get import get
from process_api.modules.selenium.set import set
from process_api.modules.selenium.wait import wait
from process_api.modules.selenium.perform import perform
from process_api.utils.get_value import get_value
from process_api.modules.selenium.modules import register as register_modules


async def get_driver(step, ctx=None, process=None, item=None):
    args = step["args"]
    return await get_value(args.get("driver"), ctx, process, item)


class SeleniumModule:
    @staticmethod
    def register(api):
        api.add_module("selenium", SeleniumModule)
        register_modules(api)

    @staticmethod
    async def init_driver(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        browser = await get_value(args.get("browser"), ctx, process, item)
        options = await get_value(args.get("options"), ctx, process, item)
        return await Driver.init(browser, options)

    @staticmethod
    async def close_driver(api, step, ctx=None, process=None, item=None):
        driver = await get_driver(step, ctx, process, item)
        await Driver.close(driver)

    @staticmethod
    async def goto(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        driver = await get_driver(step, ctx, process, item)
        url = await get_value(args.get("url"), ctx, process, item)
        await goto(driver, url)

    @staticmethod
    async def get(api, step, ctx=None, process=None, item=None):
        driver = await get_driver(step, ctx, process, item)
        return await get(driver, step["args"])

    @staticmethod
    async def set(api, step, ctx=None, process=None, item=None):
        driver = await get_driver(step, ctx, process, item)
        return await set(driver, step["args"])

    @staticmethod
    async def wait(api, step, ctx=None, process=None, item=None):
        driver = await get_driver(step, ctx, process, item)
        return await wait(driver, step["args"])

    @staticmethod
    async def perform(api, step, ctx=None, process=None, item=None):
        driver = await get_driver(step, ctx, process, item)
        return await perform(driver, step["args"])