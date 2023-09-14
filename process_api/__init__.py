from process_api.process_runner import ProcessRunner
from process_api.schema_runner import SchemaRunner
from process_api.modules import register


# This class is a wrapper around the ProcessRunner class.
# It is used to make the process_runner module more accessible.
# Since process steps can be called from anywhere in the code, including other modules,
# use the process variable to call process steps.
class ProcessAPI:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProcessAPI, cls).__new__(cls)

        return cls.instance

    def __init__(self):
        self.process_runner = ProcessRunner()
        self.schema_runner = SchemaRunner()

    def add_module(self, name, module):
        self.process_runner.modules[name] = module

    # This method is used to call a process step.
    async def call(self, step_type, step_action, step_args, ctx=None, process=None, item=None):
        step = {
            "type": step_type,
            "action": step_action,
            "args": step_args
        }

        return await self.run(step, ctx, process, item)

    async def run(self, step, ctx=None, process=None, item=None):
        return await self.process_runner.run_step(self, step, ctx, process, item)

    async def run_from_file(self, api, filename, ctx=None, parameters=None):
        return await self.schema_runner.run_from_file(api, filename, ctx, parameters)


process_api = ProcessAPI()
call = process_api.call
register(process_api)