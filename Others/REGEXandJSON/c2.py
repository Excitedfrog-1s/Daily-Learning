# coding=utf-8
'''
'Python' 普通字符  '\d' 元字符
'''
import re

a = 'C0C++7Java8C#9Python6Javascript'  # 找出所有数字
r = re.findall('\d', a)
print(r)
