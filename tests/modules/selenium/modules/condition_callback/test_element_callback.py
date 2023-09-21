import pytest
from tests.mocks.mock_web_element import MockWebElement
from process_api.modules.selenium.condition_callbacks import element_callback, element_usable_callback, light_and_shadow_dom_callback


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
    assert predicate(driver) is not False


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
    assert predicate(driver) is not False


@pytest.mark.asyncio
async def test_element_usable_callback_pass():
    element = MockWebElement(None, "div")

    predicate = element_usable_callback(element)
    assert predicate(None) is not False


@pytest.mark.asyncio
async def test_element_usable_callback_fail():
    element = MockWebElement(None, "div")
    element.enabled = False

    predicate = element_usable_callback(element)
    assert predicate(None) is None


@pytest.mark.asyncio
async def test_light_and_shadow_dom_callback_parent_pass():
    element = MockWebElement(None, "div")

    element.add_children(
        MockWebElement(None, "child1")
    )

    predicate = light_and_shadow_dom_callback(element, None, "child1")
    assert predicate(None) is not None


@pytest.mark.asyncio
async def test_light_and_shadow_dom_callback_shadow_pass():
    element = MockWebElement(None, "div")
    shadow_root = MockWebElement(None, "shadow_root")

    shadow_root.add_children(
        MockWebElement(None, "child1")
    )

    predicate = light_and_shadow_dom_callback(element, shadow_root, "child1")
    assert predicate(None) is not None


@pytest.mark.asyncio
async def test_light_and_shadow_dom_callback_fail():
    element = MockWebElement(None, "div")
    shadow_root = MockWebElement(None, "shadow_root")

    predicate = light_and_shadow_dom_callback(element, shadow_root, "child1")
    assert predicate(None) is None
