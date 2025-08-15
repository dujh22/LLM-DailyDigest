# pip install zai-sdk
from zai import ZhipuAiClient
from config2 import api_key
model = "glm-4.5"

client = ZhipuAiClient(api_key=api_key)  

def llm_chat_stream(prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
        thinking={
            "type": "enabled",    # 启用深度思考模式
        },
        stream=True,              # 启用流式输出
        max_tokens=4096,          # 最大输出tokens
        temperature=0.7           # 控制输出的随机性
    )

    # 获取回复
    for chunk in response:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end='')

def llm_chat(prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
        thinking={
            "type": "enabled",    # 启用深度思考模式
        },
        stream=False
    )
    return response.choices[0].message.content


# 主要测试函数
def main():
    print(llm_chat("你好，请问你是谁？"))
    # llm_chat_stream("你好，请问你是谁？")

if __name__ == "__main__":
    main()
    