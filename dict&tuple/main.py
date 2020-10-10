name_set = {"周", "林", "黃", "周"}
print(name_set)

# 第二種專屬技能
b = name_set.add("吳")
print(name_set)
print(b)

name_set.add("周")
print(name_set)

name_set.discard("吳")
print(name_set)

name_set.discard("謝")
print(name_set)

# 第一種專屬技能
name_set = name_set.union({"何", "周"})
print(name_set)

for n in name_set:
    print("-", n)

