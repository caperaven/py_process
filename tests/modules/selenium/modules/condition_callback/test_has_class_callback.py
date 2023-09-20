import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.modules.condition_callbacks import has_class_callback


@pytest.mark.asyncio
async def test_has_class_callback_true_pass():
    element = MockWebElement(None, "test")
    element.set_attribute("class", ["test"])

    args = {
        "class": "test",
        "present": True
    }

    predicate = has_class_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_has_class_callback_false_pass():
    element = MockWebElement(None, "test")
    element.set_attribute("class", [])

    args = {
        "class": "test",
        "present": False
    }

    predicate = has_class_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_has_class_callback_true_fail():
    element = MockWebElement(None, "test")
    element.set_attribute("class", [])

    args = {
        "class": "test",
        "present": True
    }

    predicate = has_class_callback(element, args)
    assert predicate(None) is False


@pytest.mark.asyncio
async def test_has_class_callback_false_fail():
    element = MockWebElement(None, "test")
    element.set_attribute("class", ["test"])

    args = {
        "class": "test",
        "present": False
    }

    predicate = has_class_callback(element, args)
    assert predicate(None) is False
