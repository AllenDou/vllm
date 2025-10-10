curl http://localhost:10001/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "/nasmnt/models/Llama-3.2-1B-Instruct/",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    }'

        #"stream": true,
