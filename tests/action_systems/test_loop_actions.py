import pytest
from process_api import process_api
from process_api.modules.loop import LoopModule


@pytest.mark.asyncio
async def test_loop(monkeypatch):
    data = [{"firstName": "John"}, {"firstName": "Jane"}]
    printed_message = []

    def mock_print(x):
        nonlocal printed_message
        printed_message.append(x)

    monkeypatch.setattr('builtins.print', mock_print)

    step = {
        "args": {
            "source": data,
            "process_step": {
                "type": "console",
                "action": "print",
                "args": {"message": "$i{firstName}"}
            }
        }
    }

    await LoopModule.perform(process_api, step, None, None, None)

    assert printed_message == ['John', 'Jane']