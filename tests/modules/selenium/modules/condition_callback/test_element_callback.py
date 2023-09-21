import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.condition_callbacks import element_callback


@pytest.mark.asyncio
async def test_element_callback_true_pass():
    driver = MockWebElement(None, "driver")
    driver.add_children(
        MockWebElement(None, "child1")
    )

    args = {
        "query": "test",
        "present": True
    }

    predicate = element_callback(None, args)
    assert predicate(driver) is True


@pytest.mark.asyncio
async def test_element_callback_true_fail():
    driver = MockWebElement(None, "driver")

    args = {
        "query": "test",
        "present": True
    }

    predicate = element_callback(None, args)
    assert predicate(driver) is False


@pytest.mark.asyncio
async def test_element_callback_false_fail():
    driver = MockWebElement(None, "driver")
    driver.add_children(
        MockWebElement(None, "child1")
    )

    args = {
        "query": "test",
        "present": False
    }

    predicate = element_callback(None, args)
    assert predicate(driver) is False


@pytest.mark.asyncio
async def test_element_callback_false_pass():
    driver = MockWebElement(None, "driver")

    args = {
        "query": "test",
        "present": False
    }

    predicate = element_callback(None, args)
    assert predicate(driver) is True
