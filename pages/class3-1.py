# for 回圈
# for 會搭配 in 來使用，in 後面接一個有範圍的東西
# range (5) 從 0 開始，到 4 為止
# i 是迴圈的變數可以自取,迴圈變數只能在迴圈內使用
# 迴圈變數每回合都會從範圍裡面取一個資料出來
for i in range(5):
    print(i)

# range 可以設定起質與結束質，但不會包含結束質
# range(1,5) 從 1 開始，到 4 為止
for i in range(1, 5):
    print(i)

# range 可以設定起質、結束質與間隔直，但不會包含結束值
# range(1, 10, 2) 從 1 開始，到 10 為止，每隔 2 個
for i in range(1, 10, 2):
    print(i)

# 補充random.randrange()函數
# random.randrange()函數可以隨機生成一個範圍內的整數
# random.randrange()設定傳入的參數跟range()一樣
import random

for i in range(5):
    print(random.randrange(1, 10))

# List 列表/清單/陣列
print([])  # 這是一個空的list
print([1, 2, 3])  # 這是一個包含3個元素的list
print(1, 2, 3, "a", "b", "c")  # 這是一個包含6個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個包含4個元素的list
print([1, True, "a", 1.23])  # 這是一個包含4個元素的list

# list 讀取元素，元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  # "a"

# list 取長度，也就是list中有幾個元素，不是index的最大值
l = [1, 2, 3, "a", "b", "c"]
print(len(l))  # 6

# list 走訪元素
# 可以透過取得index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取得資料
# 這兩種方式都可以，但是看使用的情境是否會需要index來決定要用哪一種方式
l = [1, 2, 3, "a", "b", "c"]

for i in range(len(L)):
    print(L[i])  # 1,2,3,a,b,c

for i in range(0, len(L), 2):  # 0,2,4
    print(L[i])  # 1,3,b

for i in L:
    print(i)  # 1,2,3,a,b,c

L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後，每次取2個元素，所以是[2,3,'b']
print(L[::2])
# 就是取index 1到3的元素，不包含index 4，所以是[2,3,'a']
print(L[1:4])
# 就是取index 1到3的元素，不包含index 4，並且每次取2個元素，所以是[2,'a']
print(L[1:4:2])
# 跟range一樣的用法，只是符號不同

# list修改元素
L = ["1,2,3", "a", "b", "c"]
l[0] = 2
print(L)  # ['2,2,3',"a","b","c"]

# call by value
a = 1
b = a  # 複製a的值給b
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會跟著改變
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 複製a的值給b，但是b跟a指向不同記憶體位置
b[0] = 2
print(a, b)

# list的append
L = [1, 2, 3]
L.append(4)  # 把4加到L的最後面
print(L)  # [1,2,3,4]

# list的移除元素方式有兩種
# 1. 使用remove，可以移除指定的元素
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個為'a'
# 代表remove會從頭開始找，找到第一個為'a'，就會移除
# 如果想要移除所有府和的元素，可以使用回圈
for i in L:
    if i == "a":
        L.remove(i)  # L.remove('a')

# 2. 使用pop，可以移除指定的index的元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除index 的元素
# 代表pop會移除指定的index的元素
# 如果不指定index，則會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)
