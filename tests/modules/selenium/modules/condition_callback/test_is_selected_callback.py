import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.modules.condition_callbacks import selected_callback


@pytest.mark.asyncio
async def test_attributes_callback_pass():
    element = MockWebElement(None, "test")
    element.set_selected(True)

    args = {
        "value": True
    }

    predicate = selected_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_attributes_callback_fail():
    element = MockWebElement(None, "test")
    element.set_selected(False)

    args = {
        "value": True
    }

    predicate = selected_callback(element, args)
    assert predicate(None) is False
