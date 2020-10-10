score = float(input("請輸入分數: "))  # float 小數 int 整數
# if score >= 60:
#     print("PASS")
# else:
#     print("FAIL")

if score >= 90:
    print("RANK A")
elif score >= 80:
    print("RANK B")
elif score >= 70:
    print("RANK C")
else:
    print("RANK D")