from src.utils.get_value import get_value


class Default:

    @staticmethod
    async def print(step, context, process, item):
        message = get_value(step.get('message'), context, process, item)
        print(message)
