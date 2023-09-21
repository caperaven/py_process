import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.condition_callbacks import has_attribute_callback


@pytest.mark.asyncio
async def test_has_attribute_callback_true_pass():
    element = MockWebElement(None, "test")
    element.set_attribute("data-value", "test")

    args = {
        "attr": "data-value",
        "present": True
    }

    predicate = has_attribute_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_has_attribute_callback_false_pass():
    element = MockWebElement(None, "test")

    args = {
        "attr": "data-value",
        "present": False
    }

    predicate = has_attribute_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_has_attribute_callback_true_fail():
    element = MockWebElement(None, "test")

    args = {
        "attr": "data-value",
        "present": True
    }

    predicate = has_attribute_callback(element, args)
    assert predicate(None) is False


@pytest.mark.asyncio
async def test_has_attribute_callback_false_fail():
    element = MockWebElement(None, "test")
    element.set_attribute("data-value", "test")

    args = {
        "attr": "data-value",
        "present": False
    }

    predicate = has_attribute_callback(element, args)
    assert predicate(None) is False
