import streamlit as st
import menu

menu.menu()
# 設定應用程式的標題
st.title("點餐機")

# 檢查 session_state 中是否已有購物車(cart)，若無則初始化為空列表
if "cart" not in st.session_state:
    st.session_state.cart = []

# 建立兩個欄位，讓使用者輸入餐點
col1, col2 = st.columns(2)
with col1:
    # 使用者輸入餐點名稱
    foodinput = st.text_input("請輸入餐點")

with col2:
    # 當使用者按下「加入」按鈕時，將餐點加入購物車
    if st.button("加入", key="add"):
        st.session_state.cart.append(foodinput)

# 顯示購物車的內容
st.write("### 購物車")
# 顯示購物車中的每一項餐點
for index in range(len(st.session_state.cart)):
    # 每一行顯示餐點，並且提供刪除按鈕
    col3, col4 = st.columns(2)
    with col3:
        # 顯示餐點名稱
        st.write(f"{st.session_state.cart[index]}")
    with col4:
        # 當使用者按下「刪除」按鈕時，刪除該項餐點
        if st.button("刪除", key=f"clear{index}"):  # 如果按鈕被按下
            st.session_state.cart.pop(index)  # 刪除購物車中的該項餐點
            st.rerun()  # 刷新頁面，顯示更新後的購物車內容
