from src.process_runner import ProcessRunner


# This class is a wrapper around the ProcessRunner class.
# It is used to make the process_runner module more accessible.
# Since process steps can be called from anywhere in the code, including other modules,
# use the process variable to call process steps.
class Process:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Process, cls).__new__(cls)

        return cls.instance

    def __init__(self, modules=None):
        self.process_runner = ProcessRunner(modules)

    async def add_module(self, name, module):
        self.process_runner.modules[name] = module

    # This method is used to call a process step.
    async def call(self, step_type, step_action, step_args, context=None, process=None, item=None):
        step = {
            "type": step_type,
            "action": step_action,
            "args": step_args
        }

        return await self.process_runner.run_step(step, context, process, item)

    async def run(self, step, context, process, item):
        return await self.process_runner.run_step(step, context, process, item)


process = Process()
call = process.call
