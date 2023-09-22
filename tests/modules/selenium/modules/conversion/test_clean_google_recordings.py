import pytest
from process_api.modules.selenium.conversions.clean_google_recording import clean_google_recording
from tests.modules.selenium.modules.conversion.recordings.google_recording import recording_key_press, recording_change, \
    recording_large


@pytest.mark.asyncio
async def test_key_press_cleanup():
    result = clean_google_recording(recording_key_press)
    assert result["steps"][0]["type"] == "keyPress"
    assert result["steps"][0]["key"] == "Tab"


@pytest.mark.asyncio
async def test_change_cleanup():
    result = clean_google_recording(recording_change)
    assert result["steps"][0]["type"] == "change"
    assert result["steps"][0]["value"] == "Hello World"
    assert result["steps"][0]["selectors"] == [
        ["container-component", "child-component", "label:nth-of-type(1) > input"]
    ]


@pytest.mark.asyncio
async def test_change_large():
    result = clean_google_recording(recording_large)

    assert result["steps"][0]["type"] == "setViewport"

    assert result["steps"][1]["type"] == "navigate"
    assert result["steps"][1]["url"] == "http://127.0.0.1:8080/web/"

    assert result["steps"][2]["type"] == "click"
    assert result["steps"][2]["selectors"] == [["[id='cbCSS']"]]

    assert result["steps"][3]["type"] == "click"
    assert result["steps"][3]["selectors"] == [['container-component', 'child-component', 'label:nth-of-type(1) > input']]

    assert result["steps"][4]["type"] == "change"
    assert result["steps"][4]["selectors"] == [['container-component', 'child-component', 'label:nth-of-type(1) > input']]
    assert result["steps"][4]["value"] == "Hello World"

    assert result["steps"][5]["type"] == "keyPress"
    assert result["steps"][5]["key"] == "Tab"

    assert result["steps"][6]["type"] == "keyPress"
    assert result["steps"][6]["key"] == "Tab"

    assert result["steps"][7]["type"] == "keyPress"
    assert result["steps"][7]["key"] == "Tab"

    assert result["steps"][8]["type"] == "keyPress"
    assert result["steps"][8]["key"] == "Enter"
