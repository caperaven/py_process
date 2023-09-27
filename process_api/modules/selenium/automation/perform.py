import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from process_api.modules.selenium.automation.get import get_element


async def perform(driver, args):
    timeout = args.get("timeout", 10)
    context = args.get("context", driver)
    query = args.get("query", None)

    # not all actions require an element
    if query is not None:
        element = await get_element(context, query, timeout)
    else:
        element = None

    action = args["action"]
    chain = ActionChains(driver)
    count = args.get("count", 1)

    await Actions.scroll_into_view(driver, element, chain, args)

    for i in range(count):
        try:
            await Actions.__dict__[action](driver, element, chain, args)
        except StaleElementReferenceException:
            time.sleep(1)
            await Actions.__dict__[action](driver, element, chain, args)
            pass


class Actions:
    @staticmethod
    async def click(driver, element, chain, args=None):
        element.click()

    @staticmethod
    async def double_click(driver, element, chain, args=None):
        action = chain.double_click(element)
        action.perform()

    @staticmethod
    async def context_click(driver, element, chain, args=None):
        action = chain.context_click(element)
        action.perform()

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

    @staticmethod
    async def hover_over_element(driver, element, chain, args):
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        pass

    @staticmethod
    async def switch_to_frame(driver, element, chain, args):
        index = args.get("index", None)

        if index is not None:
            return driver.switch_to.frame(index)

        name = args.get("name", None)
        if name is not None:
            return driver.switch_to.frame(name)

        frame_id = args.get("frame_id", None)
        if id is not None:
            frame_element = driver.find_element(By.ID, frame_id)
            return driver.switch_to.frame(frame_element)

    @staticmethod
    async def switch_to_default(driver, element, chain, args):
        try:
            driver.switch_to.default_content()
        except StaleElementReferenceException:
            time.sleep(0.25)
            await Actions.switch_to_default(driver, element, chain, args)
            pass

    @staticmethod
    async def switch_to_tab(driver, element, chain, args):
        index = args.get("index", 0)
        driver.switch_to.window(driver.window_handles[index])
