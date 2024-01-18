import os
import gc
import torch


class ModelBase:
    def __init__(self, model_name):
        self.model = None
        self.tokenizer = None
        self.model_path = None
        self.device = None
        self.model_name = model_name

    async def load(self, path):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_path = os.path.normpath(path + "/" + self.model_name)

    async def execute(self):
        if self.model is None:
            raise Exception(f"'{self.model_name}' model not loaded. Please call load_model first.")

    async def dispose(self):
        self.model = None
        self.tokenizer = None
        gc.collect()
        torch.cuda.empty_cache()

