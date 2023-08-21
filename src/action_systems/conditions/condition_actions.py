from src.utils.get_value import get_value


class Default:

    @staticmethod
    async def perform(args, context=None, process=None, item=None):
        condition = await get_value(args.get('condition'), context, process, item)
        pass_step = await get_value(args.get('pass_step'), context, process, item)
        fail_step = await get_value(args.get('fail_step'), context, process, item)


        return True
