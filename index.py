import asyncio
import src.process_api as process


asyncio.run(process.call("loop", None, {
    "source": [1, 2, 3, 4, 5],
    "process_step": {
        "type": "console",
        "action": "print",
        "args": {"message": "$i"}
    }
}))