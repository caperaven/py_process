from src.utils.get_value import get_value
from src.utils.run_step import run_step


class Default:

    @staticmethod
    async def perform(step, context=None, process=None, item=None):
        args = step.get("args")
        cases = await get_value(args.get('cases'), context, process, item)
        value = await get_value(args.get('check'), context, process, item)

        step_to_run = cases.get(value)

        if value is not None:
            await run_step(step_to_run, context, process, item)