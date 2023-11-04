import os
import gc
import torch
from transformers import GPTNeoForCausalLM, GPT2Tokenizer


class GPTNeoCache:
    def __init__(self, path):
        self.model = None
        self.tokenizer = None
        self.model_path = None
        self.device = None
        self.model_name = "EleutherAI/gpt-neo-2.7B"

    async def load(self, path):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model_path = os.path.normpath(path + "/" + self.model_name)

        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_path)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = GPTNeoForCausalLM.from_pretrained(self.model_path).to(self.device)

        return f"Using device: {self.device}"

    async def execute(self, prompt, do_sample, max_length, temperature):
        if self.model is None:
            raise Exception("GPT-Neo model not loaded. Please call load_model first.")

        inputs = self.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}  # Move inputs to GPU

        output = self.model.generate(
            input_ids=inputs['input_ids'],
            attention_mask=inputs['attention_mask'],
            pad_token_id=self.tokenizer.eos_token_id,
            do_sample=do_sample,
            temperature=temperature,
            max_length=max_length)

        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)

        return generated_text

    async def dispose(self):
        self.model = None
        self.tokenizer = None
        gc.collect()
        torch.cuda.empty_cache()


class GPTNeoModule:
    @staticmethod
    def register(api):
        api.add_module("gpt_neo", GPTNeoModule)

    @staticmethod
    async def load(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        model_path = args["path"]

        api.variables["gpt_neo_cache"] = GPTNeoCache(model_path)
        return await api.variables["gpt_neo_cache"].load(model_path)

    @staticmethod
    async def execute(api, step, ctx=None, process=None, item=None):
        args = step["args"]
        prompt = args["prompt"]

        do_sample = args.get("do_sample", True)
        max_length = args.get("max_length", 1024)
        temperature = args.get("temperature", 0.1)

        instance = api.variables.get("gpt_neo_cache", None)

        if instance is None:
            raise Exception("GPT-Neo model not loaded. Please call load_model first.")

        return await instance.execute(prompt, do_sample, max_length, temperature)

    @staticmethod
    async def dispose(api, step, ctx=None, process=None, item=None):
        instance = api.variables.get("gpt_neo_cache", None)

        if instance is None:
            return

        await instance.dispose()
        del api.variables["gpt_neo_cache"]


