import pytest
from process_api.schema_runner import process_parameters


async def test_required_parameter():
    with pytest.raises(Exception) as excinfo:
        await process_parameters({"parameters_def": {"name": {"required": True}}}, {})

    assert "Parameter 'name' is required." in str(excinfo.value)


async def test_not_string_parameter():
    with pytest.raises(Exception) as excinfo:
        await process_parameters({"parameters_def": {"name": {"type": "string"}}}, {"name": 1})

    assert "Parameter 'name' must be a string." in str(excinfo.value)


async def test_not_number_parameter():
    with pytest.raises(Exception) as excinfo:
        await process_parameters({"parameters_def": {"name": {"type": "number"}}}, {"name": "1"})

    assert "Parameter 'name' must be a number." in str(excinfo.value)


async def test_not_boolean_parameter():
    with pytest.raises(Exception) as excinfo:
        await process_parameters({"parameters_def": {"name": {"type": "boolean"}}}, {"name": "1"})

    assert "Parameter 'name' must be a boolean." in str(excinfo.value)


async def test_not_object_parameter():
    with pytest.raises(Exception) as excinfo:
        await process_parameters({"parameters_def": {"name": {"type": "object"}}}, {"name": "1"})

    assert "Parameter 'name' must be an object." in str(excinfo.value)


async def test_not_array_parameter():
    with pytest.raises(Exception) as excinfo:
        await process_parameters({"parameters_def": {"name": {"type": "array"}}}, {"name": "1"})

    assert "Parameter 'name' must be an array." in str(excinfo.value)


async def test_string_parameter():
    process = {"parameters_def": {"name": {"type": "string"}}}
    await process_parameters(process, {"name": "1"})
    assert (process["parameters"]["name"] == "1")


async def test_number_parameter():
    process = {"parameters_def": {"name": {"type": "number"}}}
    await process_parameters(process, {"name": 1})
    assert (process["parameters"]["name"] == 1)


async def test_boolean_parameter():
    process = {"parameters_def": {"name": {"type": "boolean"}}}
    await process_parameters(process, {"name": True})
    assert (process["parameters"]["name"] == True)


async def test_object_parameter():
    process = {"parameters_def": {"name": {"type": "object"}}}
    await process_parameters(process, {"name": {}})
    assert (process["parameters"]["name"] == {})


async def test_array_parameter():
    process = {"parameters_def": {"name": {"type": "array"}}}
    await process_parameters(process, {"name": [1]})
    assert (process["parameters"]["name"] == [1])

