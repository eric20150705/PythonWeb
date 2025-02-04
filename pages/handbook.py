import streamlit as st

with st.expander("day 1"):
    st.code(
        """
        # 這住解，不會被執行
        # ctrl+? 可以把框選的範圍作 快速註解/取消註解

        print("Hello World")  # print是在終端機顯示文字的指令
        # 基本回答
        print(1)  # int這是整數， -1，0，1，2，3，4，5，6，7，8，9
        print(1.0)  # float這是浮點數
        print(1.234)  # float這是浮點數
        print("apple")  # str這是字串 "sadasd123125557"，'1'
        print(True)  # bool這是布林值 True/False
        print(False)  # bool這是布林值 True/False

        print(1 + 1)  # 2
        print("1" + "1")  # 11，字串相加是串接

        # 變數
        a = 10  # 新增一個變數 (a)，把10存入變數
        # "="的功能是將右邊的值10存入左邊的a
        print(a)  # 在終端機顯示a所存的值
        a = "apple"  # 把"apple"存入a
        print(a)  # 在終端機顯示a所存的值

        # 運算子
        print(1 + 1)  # 加法
        print(1 - 1)  # 減法
        print(1 * 1)  # 乘法
        print(1 / 1)  # 除法
        print(1 // 1)  # 取商
        print(1 % 1)  # 取餘數
        print(2**3)  # 次方

        # 優先順序
        # 1.  () 括號
        # 2.  ** 次方
        # 3.  * / // %乘 除 取商 取餘數
        # 4.  + - 加 減

        
        """
    )

with st.expander("day 2"):
    st.write(
        '''
### 1. **字串格式化**
在 Python 中，您可以使用 f-string 進行字串格式化，讓變數或其他型態的資料嵌入字串中。

```python
name = "apple"
age = 18
print(f"hello, my name is {name}, I'm {age} years old")
```
- `{}` 用來插入變數或其他資料型態。

### 2. **字串長度**
可以使用 `len()` 函式來計算字串的長度。

```python
print(len("apple"))  # 輸出 5
print(len("，"))  # 輸出 1（中文字也會被計算為1個字符）
```

### 3. **型態檢查**
使用 `type()` 函式檢查變數的型態。

```python
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>
```

### 4. **型態轉換**
Python 提供多種型態轉換方法：

```python
print(int(1.0))  # float 轉 int
print(float(1))  # int 轉 float
print(str(1))  # int 轉 str
print(bool(1))  # int 轉 bool
print(int(1.234))  # float 轉 int
print(float("1.234"))  # str 轉 float
print(str(1.234))  # float 轉 str
print(bool(1.234))  # float 轉 bool
```
*注意*：如果轉換為錯誤的型態，會報錯。
```python
# print(int("hello"))  # 會報錯
```

### 5. **使用 `input()` 輸入資料**
`input()` 用來從使用者讀取輸入，會回傳字串。

```python
a = input("請輸入一些文字：")
print("輸入結束")
print(int(a) + 10)  # 必須將字串轉為整數才能進行數學運算
```

### 6. **比較運算子**
常用的比較運算子有：
- `==` 等於
- `!=` 不等於
- `>` 大於
- `<` 小於
- `>=` 大於等於
- `<=` 小於等於

```python
print(1 == 1)  # True
print(1 != 1)  # False
```

### 7. **邏輯運算子**
邏輯運算子有：
- `and`：兩個條件都為 `True` 時，結果為 `True`
- `or`：兩個條件中至少有一個為 `True` 時，結果為 `True`
- `not`：對條件取反

```python
print(True and True)  # True
print(False or True)  # True
print(not True)  # False
```

### 8. **運算符的優先順序**
Python 中運算符的優先順序為：
1. `()` 括號
2. `**` 次方
3. `* / // %` 乘除、取商、取餘數
4. `+ -` 加減
5. 比較運算子：`== != > < >= <=`
6. 邏輯運算子：`not and or`

### 9. **條件判斷 (if, elif, else)**
使用 `if`，`elif`，`else` 可以進行條件判斷：

```python
password = input("請輸入密碼：")
if password == "123456":
    print("歡迎Jerry！")
elif password == "1234567":
    print("歡迎Eric！")
else:
    print("密碼錯誤！")
```
- `elif` 可以避免多次 `if` 判斷，增加效率。

### 10. **Streamlit 基本操作**
Streamlit 是一個用來構建簡單網頁應用程式的工具：

- 顯示標題：
```python
import streamlit as st
st.title("這是一個標題")
```

- 顯示文字：
```python
st.write("這是一個用`st.write`顯示的字串")
```

- 顯示 Markdown 格式：
```python
st.write("""
* **粗體文字**
* *斜體文字*
* [連結](https://discord.com)
* 代碼塊:
```python
print("Hello Streamlit")
```
""")
```

- 數字輸入框：
```python
number = st.number_input("請輸入數字：", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是：{number}")
```

- 顯示按鈕並觸發事件：
```python
if st.button("點我"):
    st.balloons()
```

- 使用 session_state 保存狀態：
```python
import random as r
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)
st.write(f"存在於session_state的隨機數字={st.session_state.ans}")
```

### 11. **猜數字遊戲**
範例：建立一個簡單的猜數字遊戲，使用 `session_state` 保留隨機數字，並讓使用者猜數字。

```python
import streamlit as st
import random as r

st.title("猜數字遊戲")
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)

guess = st.number_input("請輸入一個數字：", step=1, min_value=1, max_value=100)

if guess == st.session_state.ans:
    st.write("恭喜你猜對了！")
    st.balloons()
elif guess > st.session_state.ans:
    st.write("猜錯了！數字太大了！")
else:
    st.write("猜錯了！數字太小了！")
```
'''
    )
