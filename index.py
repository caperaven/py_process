import asyncio


from process_api.process_api import process


asyncio.run(process.call("data", "load", {
    "name": "pokemon",
    "source": "data/pokemon.csv"
}))

asyncio.run(process.call("data", "call", {
    "name": "pokemon",
    "fn": "head"
}))
