import pytest
from src.action_systems.text_classification_actions import Default as TextClassificationActions


@pytest.mark.asyncio
async def test_text_classification():
    result = await TextClassificationActions.perform({"args": {"text": "This restaurant is awesome"}}, None, None, None)
    assert result[0]["label"] == "POSITIVE"
    assert result[0]["score"] > 0.9

    result = await TextClassificationActions.perform({"args": {"text": "This restaurant is awful"}}, None, None, None)
    assert result[0]["label"] == "NEGATIVE"
    assert result[0]["score"] > 0.9
