import pytest
from src.action_systems.console_actions import Default as ConsoleActions


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

    await ConsoleActions.print(step, None, None, None)
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

    await ConsoleActions.print(step, {'firstName': 'John'}, None, None)
    assert printed_message == 'John'
