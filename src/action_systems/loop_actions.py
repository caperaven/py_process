from src.utils.get_value import get_value
from src.process_api import process as api


class Default:

    @staticmethod
    async def perform(args, context, process, item):
        collection = await get_value(args.get("source"), context, process, item)

        if collection is None:
            return

        process_step = await get_value(args.get("process_step"), context, process, item)

        if isinstance(collection, str):
            process_step = process["steps"][process_step]

        for i in collection:
            await api.run(process_step, context, process, i)
