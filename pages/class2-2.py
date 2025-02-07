import streamlit as st
import menu

menu.menu()
st.title("這是一個標題")
st.write(
    "這是一個用`st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等"
)
st.write(
    """
這是一個用`st.write` 顯示的字串，可以處理Markdown的語法。
例如：
* **粗體文字**
* *斜體文字*
* [連結](https://discord.com/channels/1104580537592598629/1335531659159933001)
* 代碼塊:
```python
print("Hello Streamlit")
```
"""
)

# st.nuber input()
# 可以讓使用者輸入數字，設定step=1可以讓使用者只輸入整數
# min value= st.number_input("請輸入數字：",  step=1, min_value=0, max_value=100)
number = st.number_input("請輸入數字：", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是：{number}")
# value=0可以設定預設值為0

st.write("---")
st.title("練習")
number = st.number_input("請輸入分數：", step=1, min_value=0, max_value=100)
if number >= 90:
    st.write("A")
elif number >= 80:
    if number < 90:
        st.write("B")
    else:
        st.write("")
elif number >= 70:
    if number < 80:
        st.write("C")
    else:
        st.write("")
elif number >= 60:
    if number < 70:
        st.write("D")
    else:
        st.write("")
else:
    st.write("F")

st.write("---")
st.write("### 按鈕練習")
# st.button()可以在網頁上顯示一個按鈕，使用者可以點擊按鈕後，執行程式
# 如果使用者點擊按鈕，st.button()會回傳True，否則回傳False
st.button("點我", key="button1")
if st.button("點我", key="balloons"):
    st.balloons()
if st.button("點我", key="snow"):
    st.snow()
st.write("---")

st.write("---")
st.write("隨機數字")
# random.randint(1, 100)可以產生一個1到100之間的隨機整數
st.write(f"random.randint(1, 100) = {r.randint(1, 100)}")
if st.button("按我一下", key="random"):
    st.write(f"random.randint(1, 100) = {r.randint(1, 100)}")

# 透過session_state可以在將變數暫時存在瀏覽器當中，直到使用者重新整理整個網頁
# 按下元件、或是與元件互動，都不會讓session_state當中的變數消失
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)

st.write(f"存在於session_state的隨機數字={st.session_state.ans}")
