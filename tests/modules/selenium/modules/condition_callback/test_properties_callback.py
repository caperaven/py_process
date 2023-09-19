import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.modules.condition_callbacks import element_properties_callback


@pytest.mark.asyncio
async def test_attribute_callback_pass():
    element = MockWebElement(None, "test")
    element.set_property("field1", "test")

    args = {
        "properties": {
            "field1": "test"
        }
    }

    predicate = element_properties_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_attribute_callback_fail():
    element = MockWebElement(None, "test")
    element.set_property("field1", "test")

    args = {
        "properties": {
            "field1": "test2"
        }
    }

    predicate = element_properties_callback(element, args)
    assert predicate(None) is False
