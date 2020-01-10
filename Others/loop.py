'''
CONDITION = True
while CONDITION:
    print('I am while')
    CONDITION = False


counter = 1
while counter <= 10:
    counter += 1
    print(counter)
else:
    print('EOF')
'''
'''
# 主要用来遍历/循环 序列、集合和字典
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        if y == 'orange':
            break
        print(y)
else:
    print('fruit is gone')
'''
'''
a = [1, 2, 3]
for x in a:
    if x == 2:
        continue
    print(x)
else:
    print('EOF')
'''

a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0, len(a), 2):
    print(a[i])

b = a[0:len(a):2]
print(b)
