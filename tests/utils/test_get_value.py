from src.utils.get_value import get_value


# get the value as you passed it in as it does not start with a path prefix
def test_get_value_standard():
    assert get_value("1") == "1"


def test_get_value_context():
    assert get_value("$c{firstName}", {"firstName": "John"}) == "John"


def test_get_value_process():
    class Process:
        parameters = {"firstName": "John"}

    assert get_value("$p{firstName}", None, Process()) == "John"


def test_get_value_item():
    class Item:
        firstName = "John"

    assert get_value("$i{firstName}", None, None, Item()) == "John"


def test_get_value_complex_path():
    item = {
        "person": {
            "firstName": "John"
        }
    }

    assert get_value("$i{person.firstName}", None, None, item) == "John"