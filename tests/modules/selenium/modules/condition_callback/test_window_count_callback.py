import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.condition_callbacks import window_count_callback


class DriverMock:
    def __init__(self):
        self.window_handles = []


@pytest.mark.asyncio
async def test_window_count_callback_pass():
    element = MockWebElement(None, "test")

    args = {
        "count": 1
    }

    driver = DriverMock()
    driver.window_handles.append("test")

    predicate = window_count_callback(element, args)
    assert predicate(driver) is True


@pytest.mark.asyncio
async def test_window_count_callback_fail():
    element = MockWebElement(None, "test")
    element.set_style("color", "rgba(255, 0, 0, 1)")

    args = {
        "count": 1
    }

    predicate = window_count_callback(element, args)
    assert predicate(DriverMock()) is False
