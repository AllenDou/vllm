DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai --build-arg max_jobs=12 --build-arg nvcc_threads=2
# docker run -it --entrypoint=""  --gpus all vllm/vllm-openai:latest /bin/bash

