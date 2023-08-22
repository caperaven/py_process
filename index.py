import asyncio
import src.process_api as process

args = {
    "check": "$c{firstName}",
    "cases": {
        "John": {
            "type": "console",
            "action": "print",
            "args": {
                "message": "Hello John"
            }
        },
        "Jane": {
            "type": "console",
            "action": "print",
            "args": {
                "message": "Greetings Jane"
            }
        }
    }
}

asyncio.run(process.call("switch", None, args, {"firstName": "John1"}))
