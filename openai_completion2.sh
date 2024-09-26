curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "modelx",
        "prompt": ["给我讲一个3000字的故事吧?"],
        "max_tokens": 4000,
        "temperature": 0
    }'

        #"stream": true,
