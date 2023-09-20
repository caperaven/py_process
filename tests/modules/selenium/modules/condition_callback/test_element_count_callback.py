import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.modules.condition_callbacks import element_count_callback


@pytest.mark.asyncio
async def test_element_count_callback_pass():
    element = MockWebElement(None, "test")
    element.add_children(
        MockWebElement(None, "child1"),
        MockWebElement(None, "child2")
    )

    args = {
        "count": 2,
    }

    predicate = element_count_callback(element, args)
    assert predicate(None) is True


@pytest.mark.asyncio
async def test_element_count_callback_fail():
    element = MockWebElement(None, "test")

    args = {
        "count": 2,
    }

    predicate = element_count_callback(element, args)
    assert predicate(None) is False

