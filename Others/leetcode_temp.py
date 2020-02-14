import re


def a(s: str):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    print(s == s[::-1])

b = "123,sdd"
a(b)
