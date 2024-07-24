#!/bin/bash
IMAGE=registry.cn-beijing.aliyuncs.com/dsexperiment/vllm-inner:latest
DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag $IMAGE --build-arg max_jobs=12 --build-arg nvcc_threads=2
docker push $IMAGE

# docker run -it --gpus all $IMAGE /bin/bash

