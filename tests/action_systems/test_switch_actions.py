import pytest
from src.action_systems.switch_actions import Default as SwitchActions

step = {
    "args": {
        "check": "$c{firstName}",
    },
    "cases": {
        "John": {
            "type": "console",
            "action": "print",
            "args": {
                "message": "John"
            }
        },
        "Jane": {
            "type": "console",
            "action": "print",
            "args": {
                "message": "Jane"
            }
        }
    }
}


@pytest.mark.asyncio
async def test_condition_pass(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    await SwitchActions.perform(step, {"firstName": "John"}, None, None)
    assert printed_message == "John"

    await SwitchActions.perform(step, {"firstName": "Jane"}, None, None)
    assert printed_message == "Jane"