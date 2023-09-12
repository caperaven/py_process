import pytest
from process_api import process_api


@pytest.mark.asyncio
async def test_process_call(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    await process_api.call("console", "print", {"message": "Hello World"})
    assert printed_message == "Hello World"
