# a = "hellohellohello"
# b = a.replace("hello", "goodbye")
# print("不改舊的:", a)
# print("回傳新的:", b)
#
# a= a.replace("hello", "goodbye", 2)
# print(a)

# TODO: 1) 內容一樣, 大小寫也一樣
# TODO: 2) 內容一樣, 但大小寫不一樣
# TODO: 3) 內容不一樣
s1 = input("請輸入字串一: ")
s2 = input("請輸入字串二: ")
if s1 == s2:
    print("內容一樣, 大小寫也一樣")
elif s1.upper() == s2.upper():
    print("內容一樣, 但大小寫不一樣")
else:
    print("內容不一樣")