from src.utils.set_value import set_value


def test_set_value_context():
    context = {}
    set_value("$c{firstName}", "John", context, None, None)
    assert context["firstName"] == "John"


def test_set_value_process_parameters():
    process = {}
    set_value("$p{firstName}", "John", None, process, None)
    assert process["parameters"]["firstName"] == "John"


def test_set_value_process_data():
    process = {}
    set_value("$d{firstName}", "John", None, process, None)
    assert process["data"]["firstName"] == "John"


def test_set_value_item():
    item = {}
    set_value("$i{firstName}", "John", None, None, item)
    assert item["firstName"] == "John"


def test_set_value_context_nested():
    context = {}
    set_value("$c{person.firstName}", "John", context, None, None)
    assert context["person"]["firstName"] == "John"