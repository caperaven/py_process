from src.utils.get_value import get_value
from src.expressions.conditions import conditions
from src.process_api import process as api


class Default:

    @staticmethod
    async def perform(step, context=None, process=None, item=None):
        args = step.get('args')

        condition = args.get('condition')
        pass_step = await get_value(step.get('pass_step'), context, process, item)
        fail_step = await get_value(step.get('fail_step'), context, process, item)

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
