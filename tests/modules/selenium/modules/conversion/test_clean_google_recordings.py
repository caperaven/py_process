import pytest
from process_api.modules.selenium.conversions.clean_google_recording import clean_google_recording
from tests.modules.selenium.modules.conversion.recordings.google_recording import recording_key_press, recording_change, \
    recording_large, recording_click_sequence


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

    assert result["steps"][2]["type"] == "clickSequence"
    assert result["steps"][2]["sequence"][0] == ["[id='cbCSS']"]
    assert result["steps"][2]["sequence"][1] == ['container-component', 'child-component', 'label:nth-of-type(1) > input']

    assert result["steps"][3]["type"] == "change"
    assert result["steps"][3]["selectors"] == [['container-component', 'child-component', 'label:nth-of-type(1) > input']]
    assert result["steps"][3]["value"] == "Hello World"

    assert result["steps"][4]["type"] == "keyPress"
    assert result["steps"][4]["key"] == "Tab"

    assert result["steps"][5]["type"] == "keyPress"
    assert result["steps"][5]["key"] == "Tab"

    assert result["steps"][6]["type"] == "keyPress"
    assert result["steps"][6]["key"] == "Tab"

    assert result["steps"][7]["type"] == "keyPress"
    assert result["steps"][7]["key"] == "Enter"


@pytest.mark.asyncio
async def test_change_click_sequence():
    result = clean_google_recording(recording_click_sequence)
    assert result["steps"][0]["type"] == "clickSequence"
    assert result["steps"][0]["sequence"][0] == [ "container-component", "child-component", "label:nth-of-type(1) > input" ]
    assert result["steps"][0]["sequence"][1] == [ "container-component", "child-component", "label:nth-of-type(2) > input" ]
    assert result["steps"][0]["sequence"][2] == [ "container-component", "child-component", "label:nth-of-type(3) > input" ]
    assert len(result["steps"][0]["sequence"]) == 3

    assert result["steps"][1]["type"] == "doubleClickSequence"
    assert result["steps"][1]["sequence"][0] == [ "container-component", "child-component", "label:nth-of-type(1) > input" ]
    assert result["steps"][1]["sequence"][1] == [ "container-component", "child-component", "label:nth-of-type(2) > input" ]
    assert result["steps"][1]["sequence"][2] == [ "container-component", "child-component", "label:nth-of-type(3) > input" ]
    assert len(result["steps"][1]["sequence"]) == 3
