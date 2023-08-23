from transformers import pipeline

pipe = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
result = pipe(["This restaurant is awesome", "This restaurant is awful"])
print(result)



# #!pip install torch
# #!pip install transformers
# #!pip install accelerate
# #!pip install bitsandbytes
#
# # https://pypi.org/project/accelerate/
#
#
# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
#
# tokenizer = AutoTokenizer.from_pretrained("upstage/Llama-2-70b-instruct-v2")
#
# model = AutoModelForCausalLM.from_pretrained(
#     "upstage/Llama-2-70b-instruct-v2",
#     device_map="auto",
#     offload_folder="offload",
#     offload_state_dict = True,
#     torch_dtype=torch.float16,
#     rope_scaling={"type": "dynamic", "factor": 2} # allows handling of longer inputs
# )
#
# prompt = "### User:\nThomas is healthy, but he has to go to the hospital. What could be the reasons?\n\n### Assistant:\n"
# inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
# del inputs["token_type_ids"]
# streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
#
# output = model.generate(**inputs, streamer=streamer, use_cache=True, max_new_tokens=float('inf'))
# output_text = tokenizer.decode(output[0], skip_special_tokens=True)
#
# print(output_text)