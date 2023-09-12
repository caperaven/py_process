import os

from process_api.utils.set_value import set_value


class ProcessRunner:
    modules = {}

    def __init__(self):
        self.current_script_path = os.path.abspath(__file__)
        self.current_directory = os.path.dirname(self.current_script_path)

    async def run_step(self, api, step, context=None, process=None, item=None):
        system_type = step.get('type')
        action = step.get('action')

        module = None
        if system_type in self.modules:
            module = self.modules[system_type]
        else:
            Exception(f"Module {system_type} not found.")

        if action is None:
            action = "perform"

        if hasattr(module, action):
            function = getattr(module, action)
            result = await function(api, step, context, process, item)

            if "target" in step:
                await set_value(step.get('target'), result, context, process, item)

            return result
        else:
            print(f"{action} not found in the imported module.")
