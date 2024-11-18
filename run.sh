# for gu30
python3 -m vllm.entrypoints.openai.api_server --model /root/libin-Qwen1.5-32B-awq  --served-model-name modelx --disable-log-stats --quantization awq --max-num-seqs 1 --max-model-len 4096 --gpu-memory-utilization 0.95

