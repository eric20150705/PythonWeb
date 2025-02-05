import streamlit as st
import random as r

st.title("數字金字塔")
guess = st.number_input("請輸入一個整數：", step=1, min_value=1, max_value=9)


for i in range(guess):
    i = i + 1
    st.write(str(i) * i)
