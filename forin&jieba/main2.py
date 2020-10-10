import random
win = 0
lose =0
for times in range(0, 100000):
    # 準備三個門
    doors = ["羊", "羊"]
    c = random.randint(0, 2)
    doors.insert(c, "車")
    print(doors)
    # 讓參賽者挑一個門
    c = random.randint(0, 2)
    print("使用者選的: ", doors[c])
    del doors[c]
    print("剩下的門: ", doors)
    # 主持人開一隻羊出來
    doors.remove("羊")
    print("最後剩下的門: ", doors)
    # 確定是贏還輸
    if doors[0] == "車":
        win = win + 1
        print("贏了\n----------------")
    else:
        lose = lose + 1
        print("輸了\n----------------")
print("贏的次數: ", win)
print("輸的次數: ", lose)
total = win + lose
print("贏的機率: ", win/total * 100, "%")
print("輸的機率: ", lose/total * 100, "%")