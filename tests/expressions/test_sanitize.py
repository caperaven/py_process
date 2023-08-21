import pytest
from src.expressions.sanitize import sanitize, SanitizeTypes

@pytest.mark.asyncio
async def test_sanitize_simple_context():
    assert sanitize("$c{model.firstName} eq 'John'") == "return context.model.firstName == 'John'"
    assert sanitize("$c{model.firstName} ne 'John'") == "return context.model.firstName != 'John'"
    assert sanitize("$c{model.firstName} gt 'John'") == "return context.model.firstName > 'John'"
    assert sanitize("$c{model.firstName} ge 'John'") == "return context.model.firstName >= 'John'"
    assert sanitize("$c{model.firstName} lt 'John'") == "return context.model.firstName < 'John'"
    assert sanitize("$c{model.firstName} le 'John'") == "return context.model.firstName <= 'John'"

@pytest.mark.asyncio
async def test_sanitize_simple_item():
    assert sanitize("$i{firstName} eq 'John'") == "return item.firstName == 'John'"




def unknown(context=None, process=None, item=None):
    return context.model.firstName == 'John'