import os
from huggingface_hub import snapshot_download
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
        allow_patterns = args.get("allow_patterns", None)
        ignore_patterns = args.get("ignore_patterns", None)

        snapshot_download(model_name, local_dir=model_path, allow_patterns=allow_patterns, ignore_patterns=ignore_patterns)

    @staticmethod
    async def load_text_generator(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        model_name = args["model"]
        model_path = os.path.normpath(args["path"] + "/" + model_name)

        model = AutoModel.from_pretrained(model_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path)

        generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
        return generator
