from src.process_runner import ProcessRunner


# This class is a wrapper around the ProcessRunner class.
# It is used to make the process_runner module more accessible.
# Since process steps can be called from anywhere in the code, including other modules,
# use the process variable to call process steps.
class Process:
    def __init__(self):
        self.process_runner = ProcessRunner(["console"])

    # This method is used to call a process step.
    def call(self, step, context=None, process=None, item=None):
        return self.process_runner.run_step(step, context, process, item)


process = Process()
