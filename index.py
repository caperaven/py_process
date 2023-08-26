import asyncio
import src.process_api as process

args = {
    "name": "text-classification",
    "pipeline": {
        "model": "distilbert-base-uncased-finetuned-sst-2-english"
    },
    "input": "I love you"
}

result = asyncio.run(process.call("ai", "perform", args))
print(result)
