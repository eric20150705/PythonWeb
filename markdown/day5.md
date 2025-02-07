### 1. **成績登記系統**

這段程式碼展示了一個簡單的成績登記系統，使用字典（`dict`）來儲存每個學生的成績。每個學生的名字是字典的鍵（`key`），而對應的值（`value`）是一個包含科目及其成績的字典。

```python
# 成績登記系統，key是學生名字，value是學生的成績，每個科目有3個分數
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [80, 90, 100], "英文": [70, 80, 90]},
    "小美": {"國文": [80, 70, 60], "數學": [90, 80, 70], "英文": [60, 70, 80]},
    "小華": {"國文": [70, 60, 50], "數學": [80, 70, 60], "英文": [50, 60, 70]},
}
```

- **取得特定學生的成績**：
  - 取得小明的數學成績：`print(grade["小明"]["數學"])` 會輸出 `[80, 90, 100]`
  - 取得小美的第一次英文成績：`print(grade["小美"]["英文"][0])` 會輸出 `60`
  - 取得小華的第二次國文成績：`print(grade["小華"]["國文"][1])` 會輸出 `60`

---

### 2. **計算平均成績**

#### 2.1 **國文段考的平均成績**

使用 `for` 迴圈來遍歷每個學生的國文成績，計算每位學生的國文段考平均成績：

```python
for name, subject in grade.items():
    avg = sum(subject["國文"]) / len(subject["國文"])
    print(f"{name}的國文段考平均成績:{avg}")
```

#### 2.2 **每位學生的總平均成績**

計算每位學生所有科目的總平均成績：

```python
for name, subject in grade.items():
    total = 0
    for score in subject.values():
        total += sum(score)
    avg = total / 9  # 每位學生有 3 科，每科 3 次成績，所以是 9 次
    print(f"{name}的總平均成績:{avg}")
```

---

### 3. **全校各科目平均成績**

#### 步驟：

1. **找出所有科目**：先取得一個學生的科目名稱列表。

   ```python
   subjects = grade["小明"].keys()
   print(subjects)  # ['國文', '數學', '英文']
   ```
2. **建立一個字典儲存各科目成績**：

   ```python
   avg_grade = {"國文": [], "數學": [], "英文": []}
   ```
3. **逐一取出每位學生的成績，並加總到對應的科目**：

   ```python
   for subject in subjects:
       for name, score in grade.items():
           avg_grade[subject] += score[subject]
   ```
4. **計算各科目的平均成績**：

   ```python
   for subject, scores in avg_grade.items():
       avg = sum(scores) / len(scores)
       print(f"{subject}的平均成績:{avg}")
   ```

---

### 4. **與 OpenAI API 互動**

以下的程式碼展示如何使用 OpenAI API，並與其進行簡單的對話：

```python
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "你是一個小幫手，只能用繁體中文回答我的問題。"},
        {"role": "user", "content": "你好!"}
    ]
)

print(completion.choices[0].message.content)
```

這段程式會傳送一個訊息，並讓 GPT 回覆使用者的問題。

---

### 5. **使用 Streamlit 創建聊天機器人和猜謎遊戲**

Streamlit 可以讓你快速建立網頁應用，這段程式展示了如何建立一個簡單的聊天機器人與猜謎遊戲。

- **聊天機器人**：透過 `st.chat_message()` 顯示對話歷史，並接收使用者輸入。
- **猜謎遊戲**：根據使用者的猜測進行回應，只能給予“是”或“否”的提示。

以下是使用 `Streamlit` 設計的猜謎遊戲範例程式碼：

```python
import streamlit as st
from openai import OpenAI
import dotenv
import os
import menu

menu.menu()
dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("猜謎遊戲")

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    if message["role"] != "developer":
        with st.chat_message(message["role"]):
            st.write(message["content"])

message = st.chat_input("請輸入文字")  # 聊天輸入框元件

if message:
    st.session_state.history.append({"role": "user", "content": message})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "developer", "content": "只能用繁體中文回應後續對話，請跟使用者玩一場猜謎遊戲。"}]
        + st.session_state.history,
    )
    st.session_state.history.append(
        {"role": "assistant", "content": completion.choices[0].message.content}
    )
    st.rerun()
```

---

### 小結

這些範例展示了如何處理字典資料、計算平均數、使用 OpenAI API 以及如何透過 Streamlit 創建互動式應用。這些都是學習 Python 的重要步驟，能夠幫助你在不同的場景下使用 Python 進行資料處理和網頁應用開發。
