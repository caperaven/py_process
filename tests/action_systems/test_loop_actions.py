import pytest
from process_api.modules.loop import Default as LoopActions


@pytest.mark.asyncio
async def test_loop(monkeypatch):
    data = [{"firstName": "John"}, {"firstName": "Jane"}]
    printed_message = []

    def mock_print(x):
        nonlocal printed_message
        printed_message.append(x)

    monkeypatch.setattr('builtins.print', mock_print)
    await LoopActions.perform({
        "source": data,
        "process_step": {
            "type": "console",
            "action": "print",
            "args": {"message": "$i{firstName}"}
        }
    })

    assert printed_message == ['John', 'Jane']