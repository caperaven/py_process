import time
from selenium.webdriver import Keys
from src.action_systems.selenium.get import get_element


async def perform(driver, args):
    timeout = args.get("timeout", 10)
    context = args.get("context", driver)
    query = args.get("element")
    element = await get_element(context, query, timeout)
    action = args["action"]
    await Actions.__dict__[action](element, args)


class Actions:
    @staticmethod
    async def click(element, args=None):
        element.click()

    @staticmethod
    async def double_click(element, args=None):
        element.double_click()

    @staticmethod
    async def context_click(element, args=None):
        element.context_click()

    @staticmethod
    async def clear(element, args=None):
        element.clear()

    @staticmethod
    async def type(element, args):
        text = args["text"]

        element.clear()
        time.sleep(0.1)
        element.send_keys(text)
        time.sleep(0.25)
        element.send_keys(Keys.ENTER)

    @staticmethod
    async def hover(element, args=None):
        element.hover()

    @staticmethod
    async def key_down(element, args=None):
        key = args["key"]
        element.key_down(key)

    @staticmethod
    async def key_up(element, args=None):
        key = args["key"]
        element.key_up(key)

    @staticmethod
    async def scroll(element, args):
        x = args["x"]
        y = args["y"]
        element.scroll(x, y)

    @staticmethod
    async def scroll_into_view(element, args=None):
        element.scroll_into_view()

    @staticmethod
    async def scroll_by(element, args):
        x = args["x"]
        y = args["y"]
        element.scroll_by(x, y)

    @staticmethod
    async def move_to(element, args):
        x = args["x"]
        y = args["y"]
        element.move_to(x, y)

    @staticmethod
    async def move_by(element, args):
        x = args["x"]
        y = args["y"]
        element.move_by(x, y)

    @staticmethod
    async def drag_and_drop(element, args):
        target = args["target"]
        element.drag_and_drop(target)

    @staticmethod
    async def drag_and_drop_by(element, args):
        x = args["x"]
        y = args["y"]
        element.drag_and_drop_by(x, y)

    @staticmethod
    async def drag_and_drop_by_offset(element, args):
        x = args["x"]
        y = args["y"]
        element.drag_and_drop_by_offset(x, y)

    @staticmethod
    async def send_keys(element, args):
        keys = args["keys"]
        element.send_keys(keys)
