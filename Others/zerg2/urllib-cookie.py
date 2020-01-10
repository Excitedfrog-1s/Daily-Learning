import http.cookiejar
import urllib.request
# 获取Cookie并打印
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com/')
for item in cookie:
    print(item.name + '=' + item.value)

# 保存Cookie为火狐格式 另外一种为LWP: LWPCookieJar
filename = 'cookie.txt'
cookie1 = http.cookiejar.MozillaCookieJar(filename)
handler1 = urllib.request.HTTPCookieProcessor(cookie1)
opener1 = urllib.request.build_opener(handler1)
response1 = opener.open('http://www.baidu.com/')
cookie1.save(ignore_discard=True, ignore_expires=True)

# 读取Cookie再放进Request并请求网页
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com/')
print(response.read().decode('utf-8'))
