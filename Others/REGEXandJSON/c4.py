# 边界匹配
import re
qq = '10001'
# 要求4-8位
# $ 边界符
# r = re.findall('^\d{4,8}$', qq)
r = re.findall('000$', qq)
print(r)
# 组 ()中每个字符为且关系 []中每个字符为或关系
a = 'PythonPythonPythonPythonPython'
s = re.findall('(Python){3}', a)
print(s)
