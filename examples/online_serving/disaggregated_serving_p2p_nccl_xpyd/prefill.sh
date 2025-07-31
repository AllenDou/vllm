#!/bin/bash

CUDA_VISIBLE_DEVICES=0 /usr/bin/python3 /usr/local/bin/vllm serve /nasmnt/models/Llama-3.2-1B-Instruct/ --enforce-eager --host 0.0.0.0 --port 20003 --tensor-parallel-size 1 --seed 1024 --dtype float16 --max-model-len 200 --max-num-batched-tokens 200 --max-num-seqs 32 --trust-remote-code --gpu-memory-utilization 0.8 --disable-log-request --disable-log-stats --kv-transfer-config "{\"kv_connector\":\"P2pNcclConnector\",\"kv_role\":\"kv_producer\",\"kv_buffer_size\":\"1e1\",\"kv_port\":\"21001\",\"kv_connector_extra_config\":{\"proxy_ip\":\"0.0.0.0\",\"proxy_port\":\"30001\",\"http_port\":\"20003\",\"send_type\":\"PUT_ASYNC\",\"nccl_num_channels\":\"16\"}}"

