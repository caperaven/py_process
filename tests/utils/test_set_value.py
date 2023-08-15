import pytest
from src.utils.set_value import set_value


@pytest.mark.asyncio
async def test_set_value_context():
    context = {}
    await set_value("$c{firstName}", "John", context, None, None)
    assert context["firstName"] == "John"


@pytest.mark.asyncio
async def test_set_value_process_parameters():
    process = {}
    await set_value("$p{firstName}", "John", None, process, None)
    assert process["parameters"]["firstName"] == "John"


@pytest.mark.asyncio
async def test_set_value_process_data():
    process = {}
    await set_value("$d{firstName}", "John", None, process, None)
    assert process["data"]["firstName"] == "John"


@pytest.mark.asyncio
async def test_set_value_item():
    item = {}
    await set_value("$i{firstName}", "John", None, None, item)
    assert item["firstName"] == "John"


@pytest.mark.asyncio
async def test_set_value_context_nested():
    context = {}
    await set_value("$c{person.firstName}", "John", context, None, None)
    assert context["person"]["firstName"] == "John"