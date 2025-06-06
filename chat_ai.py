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

初始提示與輸出
初始提示：
請解釋為什麼天空是藍色的？

初始輸出特徵：

AI 直接簡要解釋光的散射，重點在「雷利散射」

語氣自然，但缺乏深度與脈絡結構

與人對話時，可能不夠引導性或可讀性

️⃣ 改進版提示與回應
改進提示 ️⃣（明確請求更詳細且淺顯的解釋）
提示：
請詳細解釋為什麼天空是藍色的，並用通俗易懂的語言，附上簡單的例子來說明光的散射現象。
改進後輸出：
AI 會使用較口語的語言，詳細解釋散射現象，並提供如「光打進水族箱」、「傍晚天空變紅」等例子，讓回答更親近生活。

改進提示（chain-of-thought，請求逐步推理）
提示：
請用一步一步的推理方式，詳細解釋天空為什麼呈現藍色，並且在最後給出總結。
改進後輸出：
AI 會逐步列出原因：
1️⃣ 陽光包含多種顏色
2️⃣ 光線進入大氣後產生散射
3️⃣ 藍光波長較短，散射效果最明顯
4️⃣ 最終在我們眼中呈現藍色天空
結尾還會做簡單總結，脈絡清晰。

改進提示 ️⃣（few-shot，模仿範例風格）
提示：
以下是問題與回答示例：
問題：為什麼香蕉是黃色的？
回答：香蕉含有胡蘿蔔素和花青素等色素，成熟時…
現在，請用相似的回答結構，解釋為什麼天空是藍色的。
改進後輸出：
AI 模仿示例，先概述再分析，風格統一，降低了過度個人化或風格不一致的偏見。

️⃣ 總結分析（約 150 字）
透過精煉提示，我觀察到 AI 的回答更具結構化與邏輯性。chain-of-thought 提示能有效促進分步推理，幫助使用者更容易理解；few-shot 提示則提升了輸出的風格一致性與可讀性。相比初始回答，改進後的結果語氣更親和，例子更貼近日常生活，同時避免簡短或籠統的回答偏見。整體來看，這些改進能顯著提高 AI 回應的可用性與深度。
