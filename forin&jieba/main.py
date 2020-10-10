person = {"name":"Elwing", "height":175, "handsome":True}
print(person)
print("name:", person["name"])

person["weight"] = 75
print(person)

person["height"] = 177
print(person["height"])

person["height"] = person["height"] + 3
print(person)

# 以前沒有的操作: 刪除
del person["weight"]
print(person)

# for 單個東西的暫時名字 in 群集
# {名字:資料} -> 因為有兩個，做出取捨以後，丟名字給你
for key in person:
    print("-", key, ":", person[key])