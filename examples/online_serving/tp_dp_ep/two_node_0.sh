CUDA_VISIBLE_DEVICES=0,1 VLLM_ALL2ALL_BACKEND=deepep_low_latency VLLM_USE_DEEP_GEMM=1 GLOO_SOCKET_IFNAME=eth2 NCCL_SOCKET_IFNAME=eth2 vllm serve /nasmnt/Qwen1.5-MoE-A2.7B/ --tensor-parallel-size 1 --served-model-name modelx --data-parallel-size 4 --enable-expert-parallel --data-parallel-size-local 2 --data-parallel-address 127.0.0.1 --data-parallel-rpc-port 13345 --api-server-count 2

