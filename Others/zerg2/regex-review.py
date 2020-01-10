import re
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
# 常规匹配
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
# 泛匹配
result = re.match('Hello.*Demo$', content)
# 匹配目标
result = re.match('^Hello\s(\d+)\sWorld.*Demo$', content)
# 贪婪匹配
result = re.match('^He.*(\d+).*Demo$', content)
# 非贪婪匹配
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
print(result.span())
