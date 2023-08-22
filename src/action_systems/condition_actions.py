from src.utils.get_value import get_value
from src.expressions.conditions import conditions
from src.process_api import process as api


class Default:

    @staticmethod
    async def perform(args, context=None, process=None, item=None):
        condition = args.get('condition')
        pass_step = args.get('pass_step')
        fail_step = args.get('fail_step')

        result = conditions.exec(condition, context, process, item)

        if result and pass_step:
            return await run_step(pass_step, context, process, item)

        if not result and fail_step:
            return await run_step(fail_step, context, process, item)


async def run_step(step, context, process, item):
    step_to_run = step

    if isinstance(step_to_run, str):
        step_to_run = process["steps"][step_to_run]

    await api.run(step_to_run, context, process, item)
