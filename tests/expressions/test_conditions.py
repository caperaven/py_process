import pytest
from src.expressions.conditions import conditions


@pytest.mark.asyncio
async def test_conditions_simple_context():
    expr = "$c{model.firstName} eq 'John'"
    context = {"model": {"firstName": "John"}}
    assert conditions.exec(expr, context) == True
