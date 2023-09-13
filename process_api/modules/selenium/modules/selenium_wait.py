
class WaitModule:

    @staticmethod
    def register(api):
        api.add_module("wait", WaitModule)

    @staticmethod
    async def time(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def is_ready(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def element(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def attribute(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def attributes(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def style_property(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def element_property(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def text_content(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def text_value(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def selected(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def child_count(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def element_count(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def window_count(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def idle(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def has_attribute(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def has_not_attribute(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def has_class(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def has_not_class(api, step, ctx=None, process=None, item=None):
        pass

