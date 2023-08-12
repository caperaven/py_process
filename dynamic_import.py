import importlib.util
import os


def dynamic_import(relative_path):
    caller_dir = os.path.dirname(os.path.abspath(__file__))
    module_path = os.path.join(caller_dir, relative_path)

    spec = importlib.util.spec_from_file_location("module_name", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
