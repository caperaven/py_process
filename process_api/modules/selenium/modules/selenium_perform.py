
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
        pass

    @staticmethod
    async def dbl_click(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def context_click(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def click_sequence(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def press_key(api, step, ctx=None, process=None, item=None):
        pass

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
        pass

    @staticmethod
    async def hover_over_element(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def drag_by(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def mouse_drag(api, step, ctx=None, process=None, item=None):
        pass
