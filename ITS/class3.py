# try介紹
# 在try當中可以放入可能會發生錯誤的程式碼
# except當中可以放入錯誤發生後的處理方式
# 可以有多個except，來處理不同的錯誤
# finally當中可以放入不論有沒有錯誤都會執行的程式碼
# finally可以省略, 如果要使用的話只能有一個放在最後

try:
    a = int(input("請輸入一個整數: "))
    b = int(input("請輸入另一個整數: "))
    result = a / b
    print(f"結果: {result}")
except ZeroDivisionError:
    print("除數不能為0")
except ValueError:
    print("請輸入有效的整數")
except Exception as e:
    print(f"發生錯誤: {e}")

finally:
    print("不論有沒有錯誤都會執行的程式碼")


# 檔案讀寫
# open() 開啟檔案
# r 讀取模式, 當檔案不存在時會報錯
# w 寫入模式, 覆蓋檔案內容, 當檔案不存在時會創建檔案
# a 附加模式, 在檔案末尾添加內容, 當檔案不存在時會創建檔案
# r+ 讀寫模式, 當檔案不存在時會報錯
# w+ 讀寫模式, 覆蓋檔案內容, 當檔案不存在時會創建檔案
# a+ 讀寫模式, 在檔案末尾添加內容, 當檔案不存在時會創建檔案

# math
# math.fabs(x)：計算x的絕對值 ,不論x是正數還是負數，返回的都是正數。
# math.floor(x)：將x向下取整數 （無條件捨去）。
# math.fmod(x)：用來計算x除以y的餘數，返回的結果是浮點數。
# math.ceil(x)：將x向上取整數（無條件進位）。
# math.frexp(x)：將x分解為m和n的乘積，其中m是x的尾數，n是x的指數。

# assert
# assertEqual(a, b)：簡單比較, 只檢查值是否相等
# assertis(a, b)：嚴格比較, 除了檢查值是否相等，還檢查類型是否相同
# assertin(a, b)：檢查a是否在b當中

# eval
# eval() 當中可以放入一個字串，如果字串當中有可以計算的數學式，會自動計算


# "".format() 可以用來格式化字串
# %f 可以用來格式化浮點數, %.2f 可以用來格式化浮點數到小數點後兩位
# %d 可以用來格式化整數, %05d 可以用來格式化整數到5位數 1=> 00001
# %s 可以用來格式化字串
