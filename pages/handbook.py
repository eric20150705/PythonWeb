import streamlit as st
import os
import menu

menu.menu()

# 打開markdown資料夾，取得所有檔案名稱
hd_book_files = os.listdir("markdown")
hd_book_files.sort()

# 透過迴圈，將markdown資料夾中的檔案名稱取出，並透過expander元件展開
for file_name in hd_book_files:
    with st.expander(file_name[:-3]):
        # 打開markdown資料夾中的檔案
        # 用r模式讀取，並指定utf-8編碼開啟，存到file變數當中
        with open(f"markdown/{file_name}", "r", encoding="utf-8") as file:
            text = file.read()  # 讀取檔案內容，存到text變數
            st.write(text)  # 顯示檔案
