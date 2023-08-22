import asyncio
import src.process_api as process

asyncio.run(process.call("condition", None, {
    "condition": "$c{firstName} == 'John'",
    "pass_step": {
        "type": "console",
        "action": "print",
        "args": {"message": "pass"}
    },
    "fail_step": {
        "type": "console",
        "action": "print",
        "args": {"message": "fail"}
    }
}, {"firstName": 'John'}))
