import pytest
from process_api.modules.selenium.conversions.clean_google_recording import clean_google_recording


@pytest.mark.asyncio
async def test_key_press_cleanup():
    recording = {
        "title": "Test Recording",
        "steps": [
            {
                "type": "keyDown",
                "target": "main",
                "key": "Tab"
            },
            {
                "type": "keyUp",
                "key": "Tab",
                "target": "main"
            }
        ]
    }

    result = clean_google_recording(recording)
    assert result["steps"][0]["type"] == "keyPress"
    assert result["steps"][0]["key"] == "Tab"


@pytest.mark.asyncio
async def test_change_cleanup():
    recording = {
        "title": "Test Recording",
        "steps": [
            {
                "type": "change",
                "value": "H",
                "selectors": [
                    [
                        "container-component",
                        "child-component",
                        "label:nth-of-type(1) > input"
                    ],
                    [
                        "aria/First Name"
                    ]
                ],
                "target": "main"
            },
            {
                "type": "keyUp",
                "key": "h",
                "target": "main"
            },
            {
                "type": "change",
                "value": "Hello W",
                "selectors": [
                    [
                        "container-component",
                        "child-component",
                        "label:nth-of-type(1) > input"
                    ],
                    [
                        "aria/First Name"
                    ]
                ],
                "target": "main"
            },
            {
                "type": "keyUp",
                "key": "w",
                "target": "main"
            },
            {
                "type": "change",
                "value": "Hello World",
                "selectors": [
                    [
                        "container-component",
                        "child-component",
                        "label:nth-of-type(1) > input"
                    ],
                    [
                        "aria/First Name"
                    ]
                ],
                "target": "main"
            }
        ]
    }

    result = clean_google_recording(recording)
    assert result["steps"][0]["type"] == "change"
    assert result["steps"][0]["value"] == "Hello World"
    assert result["steps"][0]["selectors"] == [
        ["container-component", "child-component", "label:nth-of-type(1) > input"]
    ]
