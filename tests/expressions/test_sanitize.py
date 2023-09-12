import pytest
from process_api.expressions.sanitize import sanitize


@pytest.mark.asyncio
async def test_sanitize_simple_context():
    assert sanitize("$c{model.firstName} eq 'John'") == "context['model']['firstName'] == 'John'"
    assert sanitize("$c{model.firstName} ne 'John'") == "context['model']['firstName'] != 'John'"
    assert sanitize("$c{model.firstName} gt 'John'") == "context['model']['firstName'] > 'John'"
    assert sanitize("$c{model.firstName} ge 'John'") == "context['model']['firstName'] >= 'John'"
    assert sanitize("$c{model.firstName} lt 'John'") == "context['model']['firstName'] < 'John'"
    assert sanitize("$c{model.firstName} le 'John'") == "context['model']['firstName'] <= 'John'"


@pytest.mark.asyncio
async def test_sanitize_simple_item():
    assert sanitize("$i{firstName} eq 'John'") == "item['firstName'] == 'John'"
