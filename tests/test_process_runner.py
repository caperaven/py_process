import pytest
from src.process_runner import ProcessRunner


@pytest.mark.asyncio
async def test_process_runner(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    runner = ProcessRunner(["console"])
    await runner.run_step({"type": "console", "action": "print", "args": {"message": "Hello World"}})
    assert printed_message == "Hello World"