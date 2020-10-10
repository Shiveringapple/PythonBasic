import random
def generate_ticket():
    ticket = set()
    while len(ticket) < 7:
        n = random.randint(1, 48)
        ticket.add(n)
    return ticket
prize = generate_ticket()
print("頭獎彩券:", prize)

times = 0
# 無窮迴圈 + 手動停止
# 使用時機: 當while的條件寫不出來的時候
while True:
    lottery = generate_ticket()
    print("我買的彩券:", lottery)
    times = times + 1
    total = 0
    for n in lottery:
        if n in prize:
            print(n, "中了")
            total = total + 1
    print("中了", total, "個數字")

    if total >= 4:
        break
print("總共買了", times, "張才中")