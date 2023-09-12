import pytest
from process_api import process_api
from process_api.modules.console import ConsoleModule

ConsoleModule.register(process_api)


@pytest.mark.asyncio
async def test_console_print(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    step = {
        "args": {
            "message": "Hello World"
        }
    }

    await ConsoleModule.print(process_api, step, None, None, None)
    assert printed_message == 'Hello World'


@pytest.mark.asyncio
async def test_console_print_context(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    step = {
        "args": {
            "message": "$c{firstName}"
        }
    }

    await ConsoleModule.print(process_api, step, {'firstName': 'John'}, None, None)
    assert printed_message == 'John'
