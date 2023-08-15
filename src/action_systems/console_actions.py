from src.utils.get_value import get_value


class Default:

    @staticmethod
    async def print(args, context, process, item):
        message = await get_value(args.get('message'), context, process, item)
        print(message)
        return True
