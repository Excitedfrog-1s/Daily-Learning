# 列表推导式 （不一定只用于推导列表）
a = [1, 2, 3, 4, 5, 6, 7, 8]
a1 = {1, 2, 3, 4, 5, 6, 7, 8}
a2 = {'1': 18, '2': 20, '3': 15}
b = [i**2 for i in a if i >= 5]  # 选择性筛选
b1 = {i**2 for i in a if i >= 5}
b2 = (key for key, value in a2.items())
print(b)
print(b1)
print(b2)
for x in b2:
    print(x)
