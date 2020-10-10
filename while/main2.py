times = 0
# 一個記憶區
result = 0
while times < 10:
    result = result + (times + 1)
    times = times + 1
print("結果", result)

lasttwo = 0
lastone = 0
times = 0
while times < 10:
    if times == 0:
        lasttwo = 0
        ans = 0
    elif times == 1:
        lastone = 1
        ans = 1
    else:
        ans = lasttwo + lastone
        lasttwo = lastone
        lastone = ans
    print("第", times + 1, "項:", ans)
    times = times + 1

times = 0
# 一個記憶區
result = 0
end = 5000
# 加到大於50才停，最後加的數字是多少
while result <= end:
    result = result + (times + 1)
    times = times + 1
print("最後加的是: ", times)