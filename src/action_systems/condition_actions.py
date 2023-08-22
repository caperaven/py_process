from src.expressions.conditions import conditions
from src.utils.run_step import run_step


class Default:

    @staticmethod
    async def perform(step, context=None, process=None, item=None):
        args = step.get("args")
        condition = args.get('condition')
        pass_step = step.get('pass_step')
        fail_step = step.get('fail_step')

        result = conditions.exec(condition, context, process, item)

        if result and pass_step:
            return await run_step(pass_step, context, process, item)

        if not result and fail_step:
            return await run_step(fail_step, context, process, item)



