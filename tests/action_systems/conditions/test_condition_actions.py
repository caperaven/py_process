import pytest
from src.action_systems.conditions.condition_actions import Default as ConditionActions

step = {
    "type": "condition",
    "args": {
        "condition": "$c{firstName} == 'John'",
    },
    "pass_step": {
        "type": "console",
        "action": "print",
        "args": {
            "message": "pass"
        }
    },
    "fail_step": {
        "type": "console",
        "action": "print",
        "args": {
            "message": "fail"
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

    context = {
        "firstName": "John"
    }

    await ConditionActions.perform(step, context, None, None)
    assert printed_message == "pass"


@pytest.mark.asyncio
async def test_condition_fail(monkeypatch):
    printed_message = None

    def mock_print(x):
        nonlocal printed_message
        printed_message = x

    monkeypatch.setattr('builtins.print', mock_print)

    context = {
        "firstName": "Jane"
    }

    await ConditionActions.perform(step, context, None, None)
    assert printed_message == "fail"
