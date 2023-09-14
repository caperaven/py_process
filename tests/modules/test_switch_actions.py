import pytest
from process_api import process_api
from process_api.modules.switch import SwitchModule

SwitchModule.register(process_api)

step = {
    "args": {
        "check": "$c{firstName}",
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
}


@pytest.mark.asyncio
async def test_condition_pass(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    await SwitchModule.perform(process_api, step, {"firstName": "John"}, None, None)
    assert printed_message == "John"

    await SwitchModule.perform(process_api, step, {"firstName": "Jane"}, None, None)
    assert printed_message == "Jane"