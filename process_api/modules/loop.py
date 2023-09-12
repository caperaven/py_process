from process_api.utils.get_value import get_value


class LoopModule:
    @staticmethod
    def register(api):
        api.add_module("loop", LoopModule)

    @staticmethod
    async def perform(api, args, context=None, process=None, item=None):
        collection = await get_value(args.get("source"), context, process, item)

        if collection is None:
            return

        process_step = await get_value(args.get("process_step"), context, process, item)

        if isinstance(collection, str):
            process_step = process["steps"][process_step]

        for i in collection:
            await api.run(process_step, context, process, i)
