# match 与 search
# match是从字符串首字母开始匹配，如果没有则为None
# search是搜索整个字符串，一旦找到就返回
# 这两个一旦匹配就会停止匹配，findall会继续
import re
'''
s = '83C72D1D8E67'
r = re.match('\d', s)
r1 = re.search('\d', s)
r2 = re.findall('\d', s)
print(r.span())  # span将返回匹配结果在原字符串位置
print(r1.group())
print(r2)
'''

s = 'life is short, i use python, i love python'
# 分组
r = re.search('life(.*)python(.*)python', s)
print(r.group(0, 1, 2))
print(r.group(1))
print(r.group(2))
print(r.groups())
r1 = re.findall('life(.*)python', s)
print(r1)
