
class AssertModule:

    @staticmethod
    def register(api):
        api.add_module("assert", AssertModule)

    @staticmethod
    async def attributes(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def attribute_eq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def attribute_neq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def has_attribute(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def has_not_attribute(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def child_count_eq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def child_count_neq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def style_property_eq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def style_property_neq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def element_property_eq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def element_property_neq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def tag_name_eq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def tag_name_neq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def text_content_eq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def text_content_neq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def value_eq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def value_neq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def variables_eq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def variables_neq(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def has_class(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def has_not_class(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def element_exists(api, step, ctx=None, process=None, item=None):
        pass

    @staticmethod
    async def element_not_exists(api, step, ctx=None, process=None, item=None):
        pass





