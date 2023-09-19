import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.modules.condition_callbacks import style_property_callback


@pytest.mark.asyncio
async def test_style_property_callback_pass():
    element = MockWebElement(None, "test")
    element.set_style("color", "rgba(255, 0, 0, 1)")

    args = {
        "property": "color",
        "value": "rgba(255, 0, 0, 1)"
    }

    predicate = style_property_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_style_property_callback_fail():
    element = MockWebElement(None, "test")
    element.set_style("color", "rgba(255, 0, 0, 1)")

    args = {
        "property": "color",
        "value": "rgba(0, 255, 0, 1)"
    }

    predicate = style_property_callback(element, args)
    assert predicate(None) is False