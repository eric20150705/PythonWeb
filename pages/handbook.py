import streamlit as st

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
