import os

from dynamic_import import dynamic_import
from src.utils.set_value import set_value


class ProcessRunner:
    modules = {}

    def __init__(self, modules):
        current_script_path = os.path.abspath(__file__)
        current_directory = os.path.dirname(current_script_path)

        if modules is not None:
            for module in modules:
                relative_path  = f"action_systems/{module}_actions.py"
                target_module_path = os.path.join(current_directory, relative_path)

                imported_module = dynamic_import(target_module_path).Default
                self.modules[module] = imported_module
                pass

    def run_step(self, step, context=None, process=None, item=None):
        system_type = step.get('type')
        action = step.get('action')
        args = step.get('args')

        module = self.modules[system_type]

        if hasattr(module, action):
            function = getattr(module, action)
            result = function(args, context, process, item)

            if "target" in step:
                set_value(step.get('target'), result, context, process, item)

            return result
        else:
            print(f"{action} not found in the imported module.")
