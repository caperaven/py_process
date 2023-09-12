from process_api.utils.get_value import get_value


class ConsoleModule:
    @staticmethod
    def register(api):
        api.add_module("console", ConsoleModule)

    @staticmethod
    async def print(api, step, context=None, process=None, item=None):
        args = step.get("args")
        message = await get_value(args.get('message'), context, process, item)
        print(message)
        return True


