from process_api.modules.selenium.automation import DriverActions, goto, get, set, wait, perform
from process_api.utils.get_value import get_value
from process_api.modules.selenium.modules import register as register_modules


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
        return await DriverActions.init(browser, options)

    @staticmethod
    async def close_driver(api, step, ctx=None, process=None, item=None):
        selenium_driver = api.get_variable("driver")
        await DriverActions.close(selenium_driver)

    @staticmethod
    async def goto(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        selenium_driver = api.get_variable("driver")
        url = await get_value(args.get("url"), ctx, process, item)

        await goto(selenium_driver, url)

        if "wait" in args:
            await wait(selenium_driver, {
                "query": args["wait"]
            })

    @staticmethod
    async def get(api, step, ctx=None, process=None, item=None):
        selenium_driver = api.get_variable("driver")

        args = step["args"]
        if "wait" in args:
            await wait(selenium_driver, {
                "query": args["wait"]
            })

        return await get(selenium_driver, step["args"])

    @staticmethod
    async def set(api, step, ctx=None, process=None, item=None):
        selenium_driver = api.get_variable("driver")

        args = step["args"]
        if "wait" in args:
            await wait(selenium_driver, {
                "query": args["wait"]
            })

        return await set(selenium_driver, step["args"])

    @staticmethod
    async def wait(api, step, ctx=None, process=None, item=None):
        selenium_driver = api.get_variable("driver")
        return await wait(selenium_driver, step["args"])

    @staticmethod
    async def perform(api, step, ctx=None, process=None, item=None):
        selenium_driver = api.get_variable("driver")
        await perform(selenium_driver, step["args"])

        args = step["args"]
        if "wait" in args:
            await wait(selenium_driver, {
                "query": args["wait"]
            })
