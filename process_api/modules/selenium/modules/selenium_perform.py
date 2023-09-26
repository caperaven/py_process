from selenium.webdriver import Keys
import time


class PerformModule:

    @staticmethod
    def register(api):
        api.add_module("perform", PerformModule)

    @staticmethod
    async def navigate(api, step, ctx=None, process=None, item=None):
        await api.call("selenium", "goto", step["args"], ctx, process, item)

    @staticmethod
    async def open_and_close_url(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def close_window(api, step, ctx=None, process=None, item=None):
        await api.call("selenium", "close_driver", step, ctx, process, item)
        pass

    @staticmethod
    async def refresh(api, step, ctx=None, process=None, item=None):
        driver = await api.call("selenium", "get_driver", step, ctx, process, item)
        driver.refresh()

    @staticmethod
    async def click(api, step, ctx=None, process=None, item=None):
        args = step["args"].copy()
        args["action"] = "click"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def dbl_click(api, step, ctx=None, process=None, item=None):
        args = step["args"].copy()
        args["action"] = "double_click"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def context_click(api, step, ctx=None, process=None, item=None):
        args = step["args"].copy()
        args["action"] = "context_click"
        await api.call("selenium", "perform", args, ctx, process, item)
        pass

    @staticmethod
    async def click_sequence(api, step, ctx=None, process=None, item=None):
        args = step["args"].copy()
        args["action"] = "click_sequence"

        sequence = args["sequence"]
        for query in sequence:
            args = step["args"].copy()
            args["query"] = query
            args["action"] = "click"
            await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def press_key(api, step, ctx=None, process=None, item=None):
        args = step["args"].copy()
        element = await api.call("selenium", "get", args, ctx, process, item)
        key_value = args["key"].upper()
        key = getattr(Keys, key_value)
        element.send_keys(key)

    @staticmethod
    async def print_screen(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def select_option(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def switch_to_frame(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def switch_to_default(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def switch_to_tab(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def type_text(api, step, ctx=None, process=None, item=None):
        args = step["args"].copy()
        value = args["value"]
        element = await api.call("selenium", "get", args, ctx, process, item)

        element.clear()
        element.send_keys(value)
        time.sleep(0.1)
        element.send_keys(Keys.ENTER)
        time.sleep(0.25)

    @staticmethod
    async def hover_over_element(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def drag_by(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def mouse_drag(api, step, ctx=None, process=None, item=None):
        pass
