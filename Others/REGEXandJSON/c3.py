# 字符集 "概括"字符集(\d->[0-9] \D->[^0-9])
# \w 单词字符 ->[A-Za-z0-9_]
# \s 空白字符
# 数量词 {x}
# * 匹配*前面的字符0次或者无限多次
# + 匹配+前面的字符1次或者无限多次
# ? 匹配?前面的字符0次或者1次

import re
a = 'pytho0python1pythonn2'
r = re.findall('python{1,2}?', a)
# t = re.findall('[a-z]{3,6}?', a)
# 贪婪（默认）与非贪婪（?）
# s = 'abc,acc,adc,aec,afc,ahc'
# r = re.findall('a[c-f]c', s)  # 从c到f的字符
# r = re.findall('a[cd]c', s) 选出acc和adc
# r = re.findall('a[^cd]c', s) 选出除了acc和adc的所有
print(r)
