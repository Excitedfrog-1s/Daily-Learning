# 正则表达式是一个特殊的字符序列，检查一个字符串是否与我们所设定的字符序列相匹配
# 如果匹配，则可快速检索文本，替换文本
# 1.检查一串数字是否是电话号码
# 2.检测一个字符串是否符合Email标准
# 3.把一个文本里指定的单词替换为另外一个单词
import re

a = 'C|C++|Java|C#|Python|Javascript'
r = re.findall('PHP', a)
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')
# print(a.index('Python') > -1)
# print('Python' in a)
# 这个常量字符串例子没有“规则”的意义
