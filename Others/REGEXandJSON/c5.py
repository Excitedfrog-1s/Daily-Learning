# 匹配模式
import re
language = 'PythonC#\nJavaPHP'
r = re.findall('c#.{1}', language, re.I | re.S)  # re.I让正则表达式忽略大小写
# |分割多个模式，re.S表示可以匹配换行符
print(r)
