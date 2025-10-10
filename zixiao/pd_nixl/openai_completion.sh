
prompt="now is `date`, The best part about working on vLLM is that I got to meet so many people across various different organizations like UCB, Google, and Meta which means"
echo $prompt
curl http://localhost:10001/v1/completions \
    -H "Content-Type: application/json" \
    -d "{
        \"model\": \"/nasmnt/models/Llama-3.2-1B-Instruct/\",
        \"prompt\": [\"$prompt\"],
        \"max_tokens\": 100,
        \"stream\": true,
        \"temperature\": 0
    }"


