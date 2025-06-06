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

初始 AI 輸出：
天空是藍色的原因是因為大氣中的空氣分子會散射陽光中的藍光。太陽光包含了各種顏色的光，但藍光的波長較短，散射的程度最大。因此，當太陽光進入大氣層時，藍光被散射到各個方向，讓我們在各個角度都能看到藍色的天空。

改進版提示與完整 AI 回覆

改進提示 1（詳細解釋、用通俗易懂的語言）
提示：
請詳細解釋為什麼天空是藍色的，並用通俗易懂的語言，附上簡單的例子來說明光的散射現象。
AI 改進後完整回覆：
天空是藍色的，主要是因為太陽光在穿過地球大氣層時，會被空氣中的小分子散射。雖然太陽光看起來是白色的，但它其實包含了七種顏色的光，像彩虹一樣。

當陽光進入大氣時，短波長的藍光比長波長的紅光更容易被散射。這種現象稱為「雷利散射」。舉個簡單的例子：想像一下你在水族箱裡打手電筒，水會讓光線變得模糊並散開。在天空中，空氣分子就像水一樣，會把藍光散射到各個方向，所以無論你往哪個方向看，天空都呈現藍色。

這也是為什麼傍晚時，當太陽位置較低，光線經過大氣層的距離變長，藍光和綠光被散射掉，剩下波長較長的紅光和橙光，讓天空看起來是紅色的原因。

改進提示 2（chain-of-thought，逐步推理）
提示：
請用一步一步的推理方式，詳細解釋天空為什麼呈現藍色，並且在最後給出總結。
AI 改進後完整回覆：
好的，我們一步一步來解釋天空為什麼是藍色的：

第一步，太陽光是白光，包含了多種顏色的光，像彩虹一樣。

第二步，當太陽光進入地球大氣層時，會與空氣中的分子發生作用，產生一種叫做「散射」的現象。

第三步，光的波長越短，散射就越強。藍光的波長比紅光短很多，因此藍光在天空中被散射得最明顯。

第四步，因為藍光被散射到各個方向，我們從任何方向看天空時，都會看到藍光，於是天空看起來是藍色的。

總結：天空之所以呈現藍色，是因為太陽光包含多種顏色，藍光的波長短，最容易被空氣中的分子散射，使我們的眼睛在各個方向都能看到藍光。

改進提示 3（few-shot，模仿範例回答結構）
提示：
以下是問題與回答示例：
問題：為什麼香蕉是黃色的？
回答：香蕉含有胡蘿蔔素和花青素等色素，成熟時，這些色素讓香蕉呈現黃色。
現在，請用相似的回答結構，解釋為什麼天空是藍色的。
AI 改進後完整回覆：
天空之所以是藍色的，是因為太陽光在進入大氣層時會被空氣分子散射。太陽光包含了多種顏色的光，其中藍光的波長較短，更容易被散射到各個方向。這種散射讓我們無論在哪個角度看天空，都能看到藍光，因此天空呈現藍色。

總結分析（約 150 字）
透過這些改進提示，AI 的回覆從簡短直述，進化為邏輯分明、條理清晰的解釋。改進提示 1 促使 AI 使用生活化的比喻和例子，讓複雜科學概念更易理解；改進提示 2 用 chain-of-thought 技巧，讓推理步驟具體呈現，幫助使用者理解科學原理；改進提示 3 的 few-shot 技巧則促進了風格穩定性，讓回答更符合專業簡潔的標準。
整體而言，這些提示優化讓 AI 回覆更豐富、準確與可讀，成功符合改進輸出品質的目標。

from openai import OpenAI
import os

client = OpenAI()

input_text = "量子力學描述微觀世界，與經典物理不同。它有疊加態、量子糾纏等特性，應用於量子計算和量子通訊。"

prompt = f"用中文，100字內簡述：{input_text}"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

summary = response.choices[0].message.content.strip()

print(summary)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)
這個簡單腳本使用 OpenAI API，將輸入文章縮寫為 100 字以內的中文摘要。執行後會印出並儲存結果，方便快速理解文章重點。
