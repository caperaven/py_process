from transformers import pipeline
from src.utils.get_value import get_value


class PipelineCache:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PipelineCache, cls).__new__(cls)

        return cls.instance

    def __init__(self):
        self.store = {}

    def get(self, name):
        return self.store.get(name, None)

    def load(self, name, pipeline_settings):
        if name in self.store:
            return self.store[name]

        self.store[name] = pipeline(**pipeline_settings)
        return self.store[name]

    def unload(self, name):
        del self.store[name]


pipeline_cache = PipelineCache()


class Default:
    @staticmethod
    async def perform(step, context=None, process=None, item=None):
        await Default.load(step, context, process, item)
        return await Default.execute(step, context, process, item)

    @staticmethod
    async def load(step, context=None, process=None, item=None):
        args = step["args"]
        name = await get_value(args.get("name"), context, process, item)
        pipeline_settings = await get_value(args.get("pipeline"), context, process, item)
        pipeline_cache.load(name, pipeline_settings)
        return True

    @staticmethod
    async def unload(step, context=None, process=None, item=None):
        args = step["args"]
        name = await get_value(args.get("name"), context, process, item)
        pipeline_cache.unload(name)
        return True

    @staticmethod
    async def execute(step, context=None, process=None, item=None):
        args = step["args"]
        pipe_input = await get_value(args.get("input"), context, process, item)

        execute = pipeline_cache.get(args.get("name"))
        if execute is None:
            raise Exception("Pipeline not loaded")

        if isinstance(pipe_input, dict):
            return execute(**pipe_input)
        else:
            return execute(pipe_input)
