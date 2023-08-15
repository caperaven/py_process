from src.action_systems.console_actions import Default as ConsoleActions


async def test_console_print(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    await ConsoleActions.print({'message': 'Hello World'}, None, None, None)
    assert printed_message == 'Hello World'


async def test_console_print_context(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    ConsoleActions.print({'message': '$c{firstName}'}, {'firstName': 'John'}, None, None)
    assert printed_message == 'John'
