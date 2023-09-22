import pytest
from process_api.modules.selenium.conversions.from_google_recording import inflate_step, selenium_lookup_table


@pytest.mark.asyncio
async def test_navigate_inflation():
    new_step = selenium_lookup_table["navigate"]
    step = inflate_step(new_step, {
        "type": "navigate",
        "url": "http://127.0.0.1:8080/web/"
    })

    assert step["type"] == "perform"
    assert step["action"] == "navigate"
    assert step["args"]["url"] == "http://127.0.0.1:8080/web/"


@pytest.mark.asyncio
async def test_click_inflation():
    new_step = selenium_lookup_table["click"]
    step = inflate_step(new_step, {
        "type": "click",
        "selectors": [
            ["container-component", "child-component", "button"]
        ]
    })

    assert step["type"] == "perform"
    assert step["action"] == "click"
    assert step["args"]["query"] == "container-component child-component button"


@pytest.mark.asyncio
async def test_type_text_inflation():
    new_step = selenium_lookup_table["change"]
    step = inflate_step(new_step, {
        "type": "change",
        "selectors": [
            ["container-component", "child-component", "button"]
        ],
        "value": "Test Input"
    })

    assert step["type"] == "perform"
    assert step["action"] == "type_text"
    assert step["args"]["query"] == "container-component child-component button"
    assert step["args"]["value"] == "Test Input"