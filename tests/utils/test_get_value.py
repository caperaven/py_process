from src.utils.get_value import get_value


# get the value as you passed it in as it does not start with a path prefix
async def test_get_value_standard():
    assert await get_value("1") == "1"


async def test_get_value_context():
    assert await get_value("$c{firstName}", {"firstName": "John"}) == "John"


async def test_get_value_process():
    class Process:
        parameters = {"firstName": "John"}

    assert await get_value("$p{firstName}", None, Process()) == "John"


async def test_get_value_item():
    class Item:
        firstName = "John"

    assert await get_value("$i{firstName}", None, None, Item()) == "John"


async def test_get_value_complex_path():
    item = {
        "person": {
            "firstName": "John"
        }
    }

    assert await get_value("$i{person.firstName}", None, None, item) == "John"