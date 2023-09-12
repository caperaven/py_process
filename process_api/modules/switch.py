from process_api.utils.run_step import run_step
from process_api.utils.get_value import get_value


class SwitchModule:

    @staticmethod
    def register(api):
        api.add_module("switch", SwitchModule)

    @staticmethod
    async def perform(api, step, context=None, process=None, item=None):
        args = step.get("args")
        cases = await get_value(args.get('cases'), context, process, item)
        value = await get_value(args.get('check'), context, process, item)

        step_to_run = cases.get(value)

        if value is not None:
            await run_step(api, step_to_run, context, process, item)
