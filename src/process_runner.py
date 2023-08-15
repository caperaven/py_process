import os

from dynamic_import import dynamic_import
from src.utils.set_value import set_value


class ProcessRunner:
    modules = {}

    def __init__(self, modules):
        self.current_script_path = os.path.abspath(__file__)
        self.current_directory = os.path.dirname(self.current_script_path)
        self.load_modules(modules)

    def load_modules(self, modules):
        if modules is not None:
            for module in modules:
                relative_path = f"action_systems/{module}_actions.py"
                target_module_path = os.path.join(self.current_directory, relative_path)

                imported_module = dynamic_import(target_module_path).Default
                self.modules[module] = imported_module
                pass

    async def run_step(self, step, context=None, process=None, item=None):
        system_type = step.get('type')
        action = step.get('action')
        args = step.get('args')

        module = None
        if system_type in self.modules:
            module = self.modules[system_type]
        else:
            self.load_modules([system_type])
            module = self.modules[system_type]

        if hasattr(module, action):
            function = getattr(module, action)
            result = await function(args, context, process, item)

            if "target" in step:
                await set_value(step.get('target'), result, context, process, item)

            return result
        else:
            print(f"{action} not found in the imported module.")
