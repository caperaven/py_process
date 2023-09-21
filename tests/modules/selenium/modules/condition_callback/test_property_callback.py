import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.condition_callbacks import element_property_callback


@pytest.mark.asyncio
async def test_attribute_callback_pass():
    element = MockWebElement(None, "test")
    element.set_property("field1", "test")

    args = {
        "property": "field1",
        "value": "test"
    }

    predicate = element_property_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_attribute_callback_fail():
    element = MockWebElement(None, "test")
    element.set_property("field1", "test")

    args = {
        "property": "field1",
        "value": "test2"
    }

    predicate = element_property_callback(element, args)
    assert predicate(None) is False
