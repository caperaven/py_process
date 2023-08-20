import pytest
from src.expressions.sanitize import sanitize, SanitizeTypes

@pytest.mark.asyncio
async def test_sanitize_simple_context():
    expr = sanitize("$c{model.firstName} eq 'John'")
    assert expr == "return context.model.firstName == 'John'"

@pytest.mark.asyncio
async def test_sanitize_simple_item():
    expr = sanitize("$i{firstName} eq 'John'")
    assert expr == "return item.firstName == 'John'"
