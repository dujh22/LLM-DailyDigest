# pip install zai-sdk
from zai import ZhipuAiClient
from config2 import api_key
model = "glm-4-flash"

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

# 带提示的对话,非流式调用
def llm_chat_with_prompt(system_prompt, user_prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        model=model,
        thinking={
            "type": "enabled",    # 启用深度思考模式
        },
        stream=False
    )
    return chat_completion.choices[0].message.content

# 主要测试函数
def main():
    # print(llm_chat("你好，请问你是谁？"))
    # llm_chat_stream("你好，请问你是谁？")
    print(llm_chat_with_prompt("你是一个翻译家，你擅长把英文翻译成中文。现在开始， 每次你收到一个英文句子或者段落，都把它翻译成地道的中文。", "who are you?"))

if __name__ == "__main__":
    main()
    