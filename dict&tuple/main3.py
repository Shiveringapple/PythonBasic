person1 = ("Elwing", 175, 75)
print(person1)

person1 = person1 + ("Taipei", )
print(person1)

print(person1[2])
print(person1[:2])

# tuple刪除? python沒有定義tuple刪除
# 不建議刪除，但可以繞彎達到
print(person1[:1] + person1[2:])