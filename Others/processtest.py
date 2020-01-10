'''
    一段小程序
'''


ACCOUNT = '123'
PASSWORD = '123456'
print('Please input account')
USER_ACCOUNT = str(input())
print('Please input password')
USER_PASSWORD = str(input())

if ACCOUNT == USER_ACCOUNT and PASSWORD == USER_PASSWORD:
    print('success')
else:
    print('fail')


a = input()
if a == 1:
    print('apple')
else:
    if a == 2:
        print('orange')
    else:
        if a == 3:
            print('banana')
        else:
            print('shopping')


a = input()
if a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a == 3:
    print('banana')
else:
    print('shopping')
