player = int(input("請選擇拳相對應的數字 [0]剪刀 [1]石頭 [2]布 : "))
import random
com = random.randint(0, 2)


trans = ["剪刀", "石頭", "布"]
# 清單名字[號碼牌]
print("玩家出的拳: ", trans[player])
print("電腦出的拳: ", trans[com])

if player == com:
    print("平手")
elif player == (com + 1) % 3:
    print("贏了")
else:
    print("輸了")