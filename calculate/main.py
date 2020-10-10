a = 3 + 3.14
print(a)

b = a * 2
print(b)

# 非常重要!
a = a * 3
print(a)

a = abs(-2 * a)  # abs 取絕對值
print(a)

a = pow(a, 2)
print(a)

# bmi: (體重) / (身高公尺) ^ 2
bmi = 79 / pow(1.76, 2)
print(bmi)