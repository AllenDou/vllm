from openai import OpenAI

# 初始化客户端（默认从环境变量 OPENAI_API_KEY 读取）
client = OpenAI(
    base_url="http://127.0.0.1:10001/v1",  # 这里设置端口号
    api_key="dummy-key"  # vLLM 默认不验证key，可以写任意字符串
)

# 或者显式传入：
# client = OpenAI(api_key="sk-xxx")

response = client.chat.completions.create(
    model="/nasmnt/models/Llama-3.2-1B-Instruct/",
    messages=[
        {"role": "system", "content": "你是一个有帮助的AI助手"},
        {"role": "user", "content": "帮我写一段Python代码，打印1到5"}
    ],
)

print(response.choices[0].message.content)

