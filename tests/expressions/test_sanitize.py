import pytest
from src.expressions.sanitize import sanitize, SanitizeTypes

@pytest.mark.asyncio
async def test_sanitize_simple():
    expr = sanitize("$c{model.firstName} eq 'John'")
    assert expr == "context.model.firstName == 'John'"
