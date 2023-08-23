from transformers import pipeline
from src.utils.get_value import get_value

DEFAULT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
DEFAULT_DEVICE = 0

class Default:

    @staticmethod
    async def perform(step, context=None, process=None, item=None):
        args = step["args"]
        text = await get_value(args.get("text"), context, process, item)
        model = await get_value(args.get("model", DEFAULT_MODEL), context, process, item)
        device = await get_value(args.get("device", DEFAULT_DEVICE), context, process, item)
        use_fast = await get_value(args.get("use_fast", True), context, process, item)
        pipe = pipeline(model=model, config=model, device=device, use_fast=use_fast)
        return pipe(text)
