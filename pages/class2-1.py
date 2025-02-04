# 字串格式化
name = "apple"
age = 18
print(f"hello,my name is {name} ,I'm {age} years old")
# 可以將變數或其他型態的資料放到f字串裡面的{} ，這樣就可以在字串中顯示

print(len("apple"))  # len()是一個函式，可計算字串的長度
print(len("，"))  # len()是一個函式，可計算字串的長度
# type() # 可以查看變數的型態
print(type(1))  #  <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>

# 型態轉換
print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(bool(1))  # int轉bool
print(int(1.234))  # float轉int
print(float("1.234"))  # float轉int
print(str(1.234))  # float轉str
print(bool(1.234))  # float轉bool
# print(int("hello"))  # 這會報錯，因為這個字串不是數字

print("輸入開始")
# input() 是一個函式，可讀取輸入
# ()裡面的文字是提示讀者輸入的內容
a = input("請輸入一些文字：")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明透過input()得到的是字串
a = int(a)
print(type(a))  # 這時候a已經是整數了


a = input("請輸入一些數字：")
print("輸入結束")
print(int(a) * int(a))


# 比較運算子
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)  # False
print(1 < 1)  #  False
print(1 >= 1)  #  True
print(1 <= 1)  #  True

# 邏輯運算子
# and 運算子
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or 運算子
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not 運算子
print(not True)  # False
print(not False)  # True

# 優先順序
# 1.  () 括號
# 2.  ** 次方
# 3.  * / // %乘 除 取商 取餘數
# 4.  + - 加 減
# 5.  == != > < >= <= 比較運算子
# 6.  not and or 邏輯運算子
