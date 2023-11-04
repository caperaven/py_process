import os
from transformers import AutoModel, AutoTokenizer, pipeline


class AIModule:
    @staticmethod
    def register(api):
        api.add_module("ai", AIModule)

    # download a model from hugging face and save it to the local cache
    @staticmethod
    async def download_model(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        model_name = args["model"]
        model_path = os.path.normpath(args["path"] + "/" + model_name)

        model = AutoModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # check if the path exists and if it does not create it.
        if not os.path.exists(model_path):
            os.makedirs(model_path)

        model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)

    @staticmethod
    async def load_text_generator(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        model_name = args["model"]
        model_path = os.path.normpath(args["path"] + "/" + model_name)

        model = AutoModel.from_pretrained(model_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path)

        generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
        return generator
