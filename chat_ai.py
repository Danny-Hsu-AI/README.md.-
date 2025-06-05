# chat_ai.py
"""
這個腳本示範如何用 OpenAI API 與 AI 模型互動。
會送出一個 prompt 給 AI，並顯示/儲存 AI 的回應。
"""

from openai import OpenAI
import os

# 取得 API Key（要先在 Colab / Shell 中 export OPENAI_API_KEY）
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("請先設定環境變數 OPENAI_API_KEY，內含你的 API Key")

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=api_key)

# 設計一個 prompt，示範與 AI 的互動
prompt = "請解釋為什麼天空是藍色的？"

# 呼叫 OpenAI API
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# 取得 AI 回覆文字
answer = response.choices[0].message.content

# 在終端機顯示
print("AI 的回覆：")
print(answer)

# 儲存到檔案
with open("ai_response.txt", "w", encoding="utf-8") as f:
    f.write(answer)
