import streamlit as st
import random as r
import menu

menu.menu()
st.title("數字金字塔")
guess = st.number_input("請輸入一個整數：", step=1, min_value=1, max_value=9)

for i in range(guess):
    i = i + 1
    st.write(str(i) * i)


st.write("---")
st.title("文字輸入元件")
# st.text_input指令格式 st.text_input(輸入欄位的標題,value="預設顯示文字")
text = st.text_input("請輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是：{text}")
