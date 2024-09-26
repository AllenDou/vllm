from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

#model_path = 'lmsys/vicuna-7b-v1.5'
#quant_path = 'vicuna-7b-v1.5-awq'
model_path = 'Qwen/Qwen2.5-14B'
quant_path = 'Qwen2.5-14B-awq'
quant_config = { "zero_point": True, "q_group_size": 32, "w_bit": 4, "version": "GEMM" }

# Load model
model = AutoAWQForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

# Quantize
model.quantize(tokenizer, quant_config=quant_config)

# Save quantized model
model.save_quantized(quant_path)
tokenizer.save_pretrained(quant_path)