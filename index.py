import asyncio
import src.process_api as process

asyncio.run(process.call("console", "print", {"message": "greetings from python"}))