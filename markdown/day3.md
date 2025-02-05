### 1. `for` 迴圈

- `for` 迴圈通常搭配 `in` 使用，`in` 會後接一個有範圍的物件（例如 `range()`、`list` 等）。
- `range()` 可以設定迴圈的範圍。基本語法：`range(結束值)`，會從 0 開始，到結束值前一個數字為止。

```python
for i in range(5):  # 0 到 4
    print(i)
```

### 2. `range()` 用法

- **設定起始值與結束值**：`range(起始值, 結束值)`，範圍會從起始值開始，到結束值前一個數字為止。
- **設定步長**：`range(起始值, 結束值, 步長)`，例如每隔 2 個數字。

```python
for i in range(1, 5):  # 1 到 4
    print(i)

for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)
```

### 3. 使用 `random.randrange()`

- `random.randrange()` 可以隨機生成一個範圍內的整數，語法與 `range()` 相似。

```python
import random

for i in range(5):
    print(random.randrange(1, 10))  # 隨機印出 1 到 9 之間的數字
```

---

### 4. List（列表、清單、陣列）

- **建立列表**：使用中括號 `[]` 建立列表，可以包含不同類型的元素。

```python
print([1, 2, 3])  # [1, 2, 3]
print([1, True, "a", 1.23])  # [1, True, 'a', 1.23]
```

- **讀取元素**：列表的索引從 0 開始。

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[3])  # "a"
```

- **計算長度**：`len()` 函數返回列表的長度（元素數量），而不是索引的最大值。

```python
print(len(L))  # 6
```

- **遍歷列表**：使用 `for` 迴圈來遍歷列表的每個元素。

```python
for i in L:
    print(i)  # 1, 2, 3, 'a', 'b', 'c'
```

- **切片（slicing）**：可以透過切片操作來取得部分資料。

```python
print(L[::2])  # 取每隔 2 個元素：[1, 3, 'b']
print(L[1:4])  # 取 index 1 到 3 的元素：[2, 3, 'a']
```

---

### 5. List 修改元素

- 可以修改列表中的元素，透過索引來進行修改。

```python
L[0] = 2
print(L)  # [2, 2, 3, 'a', 'b', 'c']
```

---

### 6. Call by Value 與 Call by Reference

- **Call by Value**：當賦值給變數時，會複製變數的值。

```python
a = 1
b = a  # 複製a的值給b
b = 2
print(a, b)  # 1, 2
```

- **Call by Reference**：當賦值給變數時，兩個變數指向相同的記憶體位置。修改其中一個變數會影響到另外一個。

```python
a = [1, 2, 3]
b = a  # a 和 b 指向同一個記憶體位置
b[0] = 2
print(a, b)  # [2, 2, 3], [2, 2, 3]
```

- **使用 `.copy()` 創建副本**：若希望複製一個列表並避免共用記憶體位置，可以使用 `.copy()`。

```python
b = a.copy()  # 複製a的內容給b，指向不同記憶體位置
b[0] = 2
print(a, b)  # [1, 2, 3], [2, 2, 3]
```

---

### 7. `append()` 方法

- `append()` 用來將元素添加到列表的尾端。

```python
L = [1, 2, 3]
L.append(4)  # 添加4
print(L)  # [1, 2, 3, 4]
```

---

### 8. 移除列表元素

- **`remove()`**：移除指定的元素，若有多個相同元素，會移除第一個。

```python
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個'a'
print(L)  # ['b', 'c', 'd', 'a']
```

- **`pop()`**：移除指定索引的元素，若不指定則移除最後一個。

```python
L.pop(0)  # 移除索引為 0 的元素
print(L)  # ['b', 'c', 'd', 'a']
```

---

### 9. Streamlit 示例程式

- **數字金字塔**：根據使用者輸入的數字顯示數字金字塔。

```python
import streamlit as st
guess = st.number_input("請輸入一個整數：", step=1, min_value=1, max_value=9)
for i in range(guess):
    st.write(str(i + 1) * (i + 1))
```

- **文字輸入元件**：展示文字輸入並顯示用戶輸入的內容。

```python
text = st.text_input("請輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是：{text}")
```

- **展示 Markdown 文件**：從 `markdown` 資料夾讀取所有 Markdown 檔案並顯示內容。

```python
import os
hd_book_files = os.listdir("markdown")
for file_name in hd_book_files:
    with st.expander(file_name[:-3]):
        with open(f"markdown/{file_name}", "r", encoding="utf-8") as file:
            text = file.read()
            st.write(text)
```
