import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.modules.condition_callbacks import attributes_callback


@pytest.mark.asyncio
async def test_attributes_callback_pass():
    element = MockWebElement(None, "test")
    element.set_attribute("data-value", "test")

    args = {
        "attributes": {
            "data-value": "test"
        }
    }

    predicate = attributes_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_attributes_callback_fail():
    element = MockWebElement(None, "test")
    element.set_attribute("data-value", "test")

    args = {
        "attributes": {
            "data-value": "invalid"
        }
    }

    predicate = attributes_callback(element, args)
    assert predicate(None) is False

