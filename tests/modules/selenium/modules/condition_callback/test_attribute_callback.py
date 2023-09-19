
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.modules.condition_callbacks import attribute_callback


async def test_attribute_callback_pass():
    element = MockWebElement(None, "test")
    element.set_attribute("data-value", "test")

    args = {
        "attr": "data-value",
        "value": "test"
    }

    predicate = attribute_callback(element, args)
    assert predicate(None) is True


async def test_attribute_callback_fail():
    element = MockWebElement(None, "test")
    element.set_attribute("data-value", "test")

    args = {
        "attr": "data-value",
        "value": "invalid"
    }

    predicate = attribute_callback(element, args)
    assert predicate(None) is False

