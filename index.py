import asyncio


from process_api import process_api


asyncio.run(process_api.call("data", "load", {
    "name": "pokemon",
    "source": "data/pokemon.csv"
}))

asyncio.run(process_api.call("data", "call", {
    "name": "pokemon",
    "fn": "head"
}))
