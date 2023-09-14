import pytest
from process_api.utils.get_value import get_value


# get the value as you passed it in as it does not start with a path prefix
@pytest.mark.asyncio
async def test_get_value_standard():
    assert await get_value("1") == "1"


@pytest.mark.asyncio
async def test_get_value_context():
    assert await get_value("$c{firstName}", {"firstName": "John"}) == "John"


@pytest.mark.asyncio
async def test_get_value_process():
    process = {"parameters": {"firstName": "John"}}
    assert await get_value("$p{firstName}", None, process) == "John"


@pytest.mark.asyncio
async def test_get_value_item():
    class Item:
        firstName = "John"

    assert await get_value("$i{firstName}", None, None, Item()) == "John"


@pytest.mark.asyncio
async def test_get_value_complex_path():
    item = {
        "person": {
            "firstName": "John"
        }
    }

    assert await get_value("$i{person.firstName}", None, None, item) == "John"


@pytest.mark.asyncio
async def test_get_objects():
    context = {}
    process = {"parameters": {}, "data": {}}
    item = {}

    assert await get_value("$c", context) == context
    assert await get_value("$p", None, process) == process["parameters"]
    assert await get_value("$d", None, process) == process["data"]
    assert await get_value("$i", None, None, item) == item