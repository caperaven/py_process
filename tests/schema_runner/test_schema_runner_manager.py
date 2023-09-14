import pytest
import os
from process_api.schema_runner import SchemaRunnerManager
from process_api import process_api


async def test_schema_runner_add_schema():
    runner = SchemaRunnerManager()
    await runner.add_schema({"id": "test"})
    assert "test" in runner.schemas

    runner.remove_schema("test")
    assert "test" not in runner.schemas

    await runner.add_schema({"id": "test"})
    await runner.clear_schemas()
    assert "test" in runner.schemas


async def test_schema_runner_add_template():
    runner = SchemaRunnerManager()
    await runner.add_template({"id": "test"})
    assert "test" in runner.templates

    runner.remove_template("test")
    assert "test" not in runner.templates

    await runner.add_template({"id": "test"})
    await runner.clear_templates()
    assert "test" in runner.templates


@pytest.mark.asyncio
async def test_schema_runner_run_process(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    schema = {
        "test_process": {
            "steps": {
                "start": {
                    "type": "console",
                    "action": "print",
                    "args": {
                        "message": "Test Message"
                    }
                }
            }
        }
    }

    runner = SchemaRunnerManager()
    await runner.run_process(process_api, schema, "test_process")
    assert printed_message == 'Test Message'


@pytest.mark.asyncio
async def test_schema_runner_run_schema(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    schema = {
        "main": {
            "steps": {
                "start": {
                    "type": "console",
                    "action": "print",
                    "args": {
                        "message": "Test Message"
                    }
                }
            }
        }
    }

    runner = SchemaRunnerManager()
    await runner.run_schema(process_api, schema, "test_process")
    assert printed_message == 'Test Message'


@pytest.mark.asyncio
async def test_schema_runner_run_from_file(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    current_directory = os.path.dirname(__file__)
    full_chrome_path = os.path.join(current_directory, "./console.json")
    full_chrome_path = os.path.normpath(full_chrome_path)

    runner = SchemaRunnerManager()
    await runner.run_from_file(process_api, full_chrome_path)
    assert printed_message == "Message from file"
