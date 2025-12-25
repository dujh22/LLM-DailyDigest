from openai import OpenAI

openai_api_key = "EMPTY"
openai_api_base = "http://127.0.0.1:8000/v1"
import json

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

def llm_chat_with_prompt(system_prompt, user_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    completion = client.chat.completions.create(
        model="zai-org/GLM-4.5",
        messages=messages,
        max_tokens=4096,    
        temperature=0.0,
        stream=False
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    print(llm_chat_with_prompt("请将中文翻译成英文,并扩写一个故事,放到一个json中", "你好，世界。"))