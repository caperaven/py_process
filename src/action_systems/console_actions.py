from src.utils.get_value import get_value


class Default:

    @staticmethod
    async def print(step, context=None, process=None, item=None):
        args = step.get("args")
        message = await get_value(args.get('message'), context, process, item)
        print(message)
        return True
