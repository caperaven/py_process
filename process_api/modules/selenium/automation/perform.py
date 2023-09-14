import time
from selenium.webdriver import Keys, ActionChains
from process_api.modules.selenium.automation.get import get_element


async def perform(driver, args):
    timeout = args.get("timeout", 10)
    context = args.get("context", driver)
    query = args.get("query")
    element = await get_element(context, query, timeout)
    action = args["action"]
    chain = ActionChains(driver)
    count = args.get("count", 1)

    await Actions.scroll_into_view(driver, element, chain, args)

    for i in range(count):
        await Actions.__dict__[action](driver, element, chain, args)
        time.sleep(0.1)


class Actions:
    @staticmethod
    async def click(driver, element, chain, args=None):
        element.click()

    @staticmethod
    async def double_click(driver, element, chain, args=None):
        element.double_click()

    @staticmethod
    async def context_click(driver, element, chain, args=None):
        element.context_click()

    @staticmethod
    async def clear(driver, element, chain, args=None):
        element.clear()

    @staticmethod
    async def type(driver, element, chain, args):
        text = args["text"]

        element.clear()
        time.sleep(0.1)
        element.send_keys(text)
        time.sleep(0.25)
        element.send_keys(Keys.ENTER)

    @staticmethod
    async def hover(driver, element, chain, args=None):
        chain.move_to_element(element).perform()

    @staticmethod
    async def key_down(driver, element, chain, args=None):
        key = args["key"]
        chain.key_down(key).perform()

    @staticmethod
    async def key_up(driver, element, chain, args=None):
        key = args["key"]
        chain.key_up(key).perform()

    @staticmethod
    async def scroll_into_view(driver, element, chain, args):
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    async def move_to(driver, element, chain, args):
        # get current position
        current_x = element.location["x"]
        current_y = element.location["y"]

        # get target position
        x = args["x"]
        y = args["y"]

        # calculate offset
        offset_x = x - current_x
        offset_y = y - current_y

        # move to target
        chain.click_and_hold(element).move_by_offset(offset_x, offset_y).release().perform()

    @staticmethod
    async def move_by(driver, element, chain, args):
        x = args["x"]
        y = args["y"]
        chain.drag_and_drop_by_offset(element, x, y).perform()

    @staticmethod
    async def drag_and_drop(driver, element, chain, args):
        target = args["target"]
        element.drag_and_drop(target)

    @staticmethod
    async def drag_and_drop_by(driver, element, chain, args):
        x = args["x"]
        y = args["y"]
        element.drag_and_drop_by(x, y)

    @staticmethod
    async def drag_and_drop_by_offset(driver, element, chain, args):
        x = args["x"]
        y = args["y"]
        element.drag_and_drop_by_offset(x, y)

    @staticmethod
    async def send_keys(driver, element, chain, args):
        keys = args["keys"]
        element.send_keys(keys)
