'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
print(driver.page_source)
'''

import requests
'''
response = requests.get('http://www.baidu.com')
response.encoding = 'utf-8'
print(response.text)
print(response.headers)
print(response.status_code)
'''
headers = {('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chr'
            'ome/70.0.3538.77 Safari/537.36')}
response = requests.get('http://www.baidu.com', headers=headers)
response.encoding = 'utf-8'
print(response.status_code)
