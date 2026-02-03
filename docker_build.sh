#!/bin/sh
REPO=vllm-funasr
DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag dsexperiment/${REPO}:latest -f docker/Dockerfile --build-arg max_jobs=64 --build-arg nvcc_threads=1

docker tag dsexperiment/${REPO}:latest datascience-registry-vpc.ap-southeast-1.cr.aliyuncs.com/dsexperiment/${REPO}:latest

docker push datascience-registry-vpc.ap-southeast-1.cr.aliyuncs.com/dsexperiment/${REPO}:latest

