# coding=utf-8

import random
import copy

'''
# g = Generator
# r = Remainder
'''


def Initr(information, g):
    i = len(g)
    r = information[:i]
    while i < len(information):
        if len(r) != len(g):
            r.append(information[i])
            i += 1
        if r[0] == 0:
            del r[0]
            continue
        for j in range(len(g)):
            r[j] = r[j] ^ g[j]
    k = 0
    for i in range(len(r)):
        if r[k] != 0:
            break
        k += 1
    r = r[k:]
    while len(r) < n:
        r.insert(0, 0)
    return r


def ErrorChannel(coded):
    i = 0
    received = copy.copy(coded)
    for i in range(len(coded)):
        p = random.random()
        if p <= 0.1:  # possibilities
            received[i] = 1 - received[i]
    return received


def CrcCheck(received, g):
    i = len(g)
    check = received[:4]
    while i < len(received):
        if len(check) != len(g):
            check.append(received[i])
            i += 1
        if check[0] == 0:
            del check[0]
            continue
        for j in range(len(g)):
            check[j] = check[j] ^ g[j]
    k = 0
    for k in range(len(check)):
        if check[k] != 0:
            return False
    return True


result = [0, 0, 0]
for i in range(100000):
    information = []
    infolength = 10   # The value of N
    g = [1, 0, 0, 1]  # Generator
    n = 3
    for i in range(infolength):
        rand = random.randint(0, 1)
        information.append(rand)
    for i in range(n):
        information.append(0)
    r = Initr(information, g)
    coded = copy.copy(information[:-3])
    for i in range(len(r)):
        coded.append(r[i])
    received = ErrorChannel(coded)
    Check = CrcCheck(received, g)
    if (coded == received) & Check:
        result[0] = result[0] + 1
    elif (coded != received) & Check:
        result[1] = result[1] + 1
    elif (coded != received) & (not Check):
        result[2] = result[2] + 1

print('Event A probability', float(result[0]) / float(sum(result)))
print('Event B probability', float(result[2]) / float(sum(result)))
print('Event C probability', float(result[1]) / float(sum(result)))
