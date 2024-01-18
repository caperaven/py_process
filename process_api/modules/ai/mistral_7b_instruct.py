from process_api.modules.ai.model_base import ModelBase
from transformers import AutoModelForCausalLM, AutoTokenizer


class MistralCache(ModelBase):
    def __init__(self):
        super().__init__("TheBloke/openbuddy-mistral-7B-v13.1-GPTQ")

    async def load(self, path):
        await super().load(path)

        self.model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
        self.tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

        # self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        # self.tokenizer.pad_token = self.tokenizer.eos_token
        # self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

        return f"Using device: {self.device}"

    async def execute(self, prompt, messages, do_sample, max_length, temperature):
        await super().execute()
        encodeds = self.tokenizer.apply_chat_template(messages, return_tensors="pt")

        model_inputs = encodeds.to(self.device)
        self.model.to(self.device)

        generated_ids = self.model.generate(model_inputs, max_new_tokens=max_length, do_sample=do_sample, temperature=temperature)
        decoded = self.tokenizer.batch_decode(generated_ids)
        return decoded[0]


class MistralModule:
    @staticmethod
    def register(api):
        api.add_module("mistral", MistralModule)

    @staticmethod
    async def load(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        model_path = args["path"]

        api.variables["mistral"] = MistralCache()
        return await api.variables["mistral"].load(model_path)

    @staticmethod
    async def execute(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        prompt = args["prompt"]

        do_sample = args.get("do_sample", False)
        max_length = args.get("max_length", 1024)
        temperature = args.get("temperature", 0.1)

        instance = api.variables.get("mistral", None)

        if instance is None:
            raise Exception("mistral model not loaded. Please call load_model first.")

        return await instance.execute(prompt, do_sample, max_length, temperature)

    @staticmethod
    async def dispose(api, step, ctx=None, process=None, item=None):
        instance = api.variables.get("mistral", None)

        if instance is None:
            return

        await instance.dispose()
        del api.variables["mistral"]