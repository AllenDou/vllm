curl http://localhost:10001/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "/nasmnt/models/Llama-3.2-1B-Instruct/",
        "prompt": [
        "NewYork is a "
        ],
        "max_tokens": 20,
        "stream": true,
        "temperature": 0
    }' 


