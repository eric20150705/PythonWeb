import streamlit as st
import menu

menu.menu()
st.title("欄位元件")
col1, col2 = st.columns(2)  # 2columns
col1.button("按鈕1", key="btn1")  # 在col1中建立一個按鈕類似st.button
col2.button("按鈕2", key="btn2")  # 在col2中建立一個按鈕類似st.button

# 2columns, 可以用比例來設定每個column的寬度,將比例放到list中
col1, col2 = st.columns([1, 2])
col1.button("按鈕1", key="btn3")  # 在col1中建立一個按鈕類似st.button
col2.button("按鈕2", key="btn4")  # 在col2中建立一個按鈕類似st.button

# 3colums
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕1", key="btn5")  # 在col1中建立一個按鈕類似st.button
col2.button("按鈕2", key="btn6")  # 在col2中建立一個按鈕類似st.button
col3.button("按鈕3", key="btn7")  # 在col3中建立一個按鈕類似st.button

col1, col2 = st.columns([1, 2])
with col1:  # 在col1中建立一個按鈕類似
    if st.button("按鈕1", key="btn8"):  # 在col1中建立一個按鈕
        st.balloons()  # 在col1中建立一個氣球
    st.write("這是col1")  # 在col1中建立一個文字
with col2:  # 在col2中建立一個按鈕類似
    st.button("按鈕2", key="btn9")  # 在col2中建立一個按鈕
    st.write("這是col2")  # 在col2中建立一個文字

# 多個columns
col_num = st.number_input("輸入欄位數量", min_value=1)
cols = st.columns(col_num)  # 4columns, cols[0]...cols[3]
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+10}")  # 在col1中建立一個按鈕類似
    # st.balloons()  # 在col1中建立一個氣球

st.markdown("---")
st.title("columns排列元件效果比較")
# 2columns
col1, col2 = st.columns(2)
with col1:
    st.button("按鈕1", key="1")
    st.button("按鈕2", key="2")
    st.button("按鈕3", key="3")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")

st.write("---")

for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"1{i+4}")
    with col2:
        st.write(f"這是col2{i+1}")

st.write("---")
if st.button("重新整理", key="button"):  # 如果按下重新整理按鈕
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面
