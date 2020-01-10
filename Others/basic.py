#Git测试
print('git')
a = 1 + 1
print(a)
b = 2 + a
print(b)

###变量
A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3]
C = A * 3 + B
print(A)
print(B)
print(C)
#--------------------------------------
a = 1
b = a
a = 3
print(b)
a = [1, 2, 3, 4, 5]
b = a
a[0] = '1'
print(a)
print(b)
a = 'hello'
id(a)
a = a + 'python'
id(a)
print(a)
#int为值类型 list为引用类型
a = [1, 2, 3]
id(a)
a[0] = '1'
id(a)
a = [1, 2, 3]
a.append(4)
print(a)
a = (1, 2, 3, [1, 2, 4])
a[3][2] = '4'
print(a)
a = (1, 2, 3, [1, 2, ['a', 'b', 'c']])
print(a[3][2][1])

#运算符
#---算数运算符
'hello' + 'world'
a = 2 * 3 % 2 + 2**2 + 2**5 / 3 // 2
#---赋值运算符
c = 1
c = c + 1
c += 1
print(c)
b = 2
a = 3
b -= a
print(b)
a = 1
b = 2
print(a + b)
#---比较运算符
1 == 2
1 >= 1
b = 1
b = b + True
b += b >= 1
print(b)
'a' > 'b'
[3, 2, 3] < [2, 3, 8]
#---逻辑运算符
True and False
True or False
not False
not not True
1 and 1
not '0'
#---成员运算符 是否在另外一组元素 返回布尔类型
a = 8
b = [1, 2, 3, 4, 5]
a not in b
b = 'c'
b in {'c': 1}
#---身份运算符 is比较的是两个变量身份是否相等
a = 1
b = 1.0
a == b
a = {1, 2, 3}
b = {2, 1, 3}
a is b
c = (1, 2, 3)
d = (2, 1, 3)
c == d
a = 'hello'
isinstance(a, str)
isinstance(a, (int, float))
#---位运算符 & | ^ ~ << >>
a = 2
b = 3
a & b
a | b

#表达式
a = 1
b = 2
c = 2
not a or b + 2 == c
not (a or b) + 2 == c
(not a) or ((b + 2) == c)
print(a + b * c)
print(a or b) and c

#流程控制 （条件 循环 分支）
mood = False
if mood:
    print('go to left')
else:
    print('go to right')