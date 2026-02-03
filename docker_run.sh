#!/bin/sh

# python3 -m vllm.entrypoints.openai.api_server --dtype bfloat16 --gpu-memory-utilization=0.1 --trust-remote-code --served-model-name modelx --disable-log-stats --max-num-seqs 16 --max-model-len 1024 --model /nasmnt/models/qwen2lm/

docker run -it -p 8000:8000 --gpus=all --entrypoint="" -v /nasmnt:/nasmnt datascience-registry-vpc.ap-southeast-1.cr.aliyuncs.com/dsexperiment/vllm-funasr:latest /bin/bash
