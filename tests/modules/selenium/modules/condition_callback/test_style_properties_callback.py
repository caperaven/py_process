import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.condition_callbacks import style_properties_callback


@pytest.mark.asyncio
async def test_style_properties_callback_pass():
    element = MockWebElement(None, "test")
    element.set_style("color", "rgba(255, 0, 0, 1)")

    args = {
        "properties": {
            "color": "rgba(255, 0, 0, 1)"
        }
    }

    predicate = style_properties_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_style_properties_callback_fail():
    element = MockWebElement(None, "test")
    element.set_style("color", "rgba(0, 255, 0, 1)")

    args = {
        "properties": {
            "color": "rgba(255, 0, 0, 1)"
        }
    }

    predicate = style_properties_callback(element, args)
    assert predicate(None) is False
