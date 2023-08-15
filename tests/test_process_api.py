from src.process_api import process


async def test_process_call(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    await process.call("console", "print", {"message": "Hello World"})
    assert printed_message == "Hello World"
