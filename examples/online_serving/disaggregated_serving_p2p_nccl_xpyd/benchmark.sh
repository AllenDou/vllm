#!/bin/bash

python3 ../../../benchmarks/benchmark_serving.py --port 10001 --seed 0 --model /nasmnt/models/Llama-3.2-1B-Instruct/  --dataset-name random --random-input-len 20 --random-output-len 100 --num-prompts 100 --burstiness 100 --request-rate 2
