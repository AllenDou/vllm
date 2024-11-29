from vllm import LLM
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, HqqConfig

model_path = "/root/zixiao/Qwen2.5-7B-Instruct"
quant_config = HqqConfig(nbits=4, group_size=64, axis=1)

model = AutoModelForCausalLM.from_pretrained(model_path,
                                             torch_dtype=torch.float16,
                                             cache_dir='.',
                                             device_map="cuda:0",
                                             quantization_config=quant_config,
                                             low_cpu_mem_usage=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

qp = "/root/zixiao/Qwen2.5-7B-Instruct_hqq"
model.save_pretrained(qp)
tokenizer.save_pretrained(qp)

llm = LLM(model=qp)
