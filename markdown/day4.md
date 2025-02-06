### Python 課程筆記：Streamlit 與基本 Python 操作

---

#### **1. Streamlit 欄位元件 (Columns)**

在 Streamlit 中，`st.columns` 用於創建多個欄位，可以讓你的應用程式界面呈現分欄效果。

##### 基本操作：

```python
import streamlit as st

# 創建兩個欄位
col1, col2 = st.columns(2)
col1.button("按鈕1", key="btn1")  # 在col1中建立一個按鈕
col2.button("按鈕2", key="btn2")  # 在col2中建立一個按鈕
```

##### 設定欄位比例：

可以將欄位寬度設為不同的比例來調整其顯示比例。

```python
col1, col2 = st.columns([1, 2])
col1.button("按鈕1", key="btn3")  # 在col1中建立一個按鈕
col2.button("按鈕2", key="btn4")  # 在col2中建立一個按鈕
```

##### 多欄位：

```python
# 創建三個欄位，並設置比例
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕1", key="btn5")
col2.button("按鈕2", key="btn6")
col3.button("按鈕3", key="btn7")
```

##### 在每個欄位內進行操作：

```python
col1, col2 = st.columns([1, 2])
with col1:
    if st.button("按鈕1", key="btn8"):
        st.balloons()  # 顯示氣球動畫
    st.write("這是col1")  # 顯示文字

with col2:
    st.button("按鈕2", key="btn9")
    st.write("這是col2")
```

##### 動態欄位數量：

根據用戶輸入的數字來動態生成欄位：

```python
col_num = st.number_input("輸入欄位數量", min_value=1)
cols = st.columns(col_num)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+10}")
```

---

#### **2. 算術運算子與優先順序**

##### 算術運算子：

```python
a = 1
a += 1  # a = a + 1
print(a)  # 2

a -= 1  # a = a - 1
print(a)  # 1

a *= 2  # a = a * 2
print(a)  # 2

a /= 2  # a = a / 2
print(a)  # 1.0

a //= 2  # a = a // 2
print(a)  # 0

a %= 2  # a = a % 2
print(a)  # 0.0

a **= 2  # a = a ** 2
print(a)  # 1.0
```

##### 運算優先順序：

1. 括號 `()`
2. 次方 `**`
3. 乘、除、取商、取餘數 `* / // %`
4. 加、減 `+ -`
5. 比較運算子 `== != > < >= <=`
6. 邏輯運算子 `not and or`
7. 算術指定運算子 `= += -= *= /= //= %= **=`

---

#### **3. while 迴圈與 break**

`while` 迴圈會持續執行，直到條件式變為 `False`。

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

##### 使用 `break` 來強制跳出迴圈：

```python
i = 0
while i < 5:
    print(i)
    if i == 3:
        break  # 跳出迴圈
    i += 1
```

---

#### **4. 字典 (Dictionary)**

字典是由 `key` 和 `value` 组成，`key` 是唯一的。

##### 基本操作：

```python
d = {"a": 1, "b": 2, "c": 3}

# 取得所有key
print(d.keys())  # dict_keys(['a', 'b', 'c'])

# 取得所有value
print(d.values())  # dict_values([1, 2, 3])

# 取得所有key-value
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# 新增或修改key-value
d["d"] = 4  # 新增
d["a"] = 5  # 修改
```

##### 檢查字典是否包含某個 `key`：

```python
print("a" in d)  # True
print("e" in d)  # False
```

##### 刪除 `key-value`：

```python
# 使用 pop() 方法刪除
print(d.pop("a"))  # 5
print(d.pop("e", ""))  # "Not found" (如果 key 不存在，返回預設值)
```

##### 複雜字典操作：

```python
d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}

print(d["a"])  # [1, 2, 3]
print(d["a"][0])  # 1
print(d["b"])  # {'c': 4, 'd': 5}
print(d["b"]["c"])  # 4
```

---

#### **5. 重新整理頁面**

使用 `st.rerun()` 重新整理 Streamlit 頁面：

```python
import time

if st.button("重新整理", key="button"):
    st.success("準備重新整理")
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理頁面
```
