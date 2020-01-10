'''
In this question, the number is not big enough.
So I limit the search range of primes between 1 to 100.
'''

def find_prime(n):
    '''
    Find p and q
    '''
    for p in range(1, 100):
        for q in range(1, 100):
            if p * q == n:
                return p, q


def check_primes(x):
    '''
    Check If They Are Primes
    '''
    for i in range(2, x):
        if x % i == 0:
            flag = 0
            break
    else:
        flag = 1
    return flag


def find_d(e, z):
    '''
    Find the Private Key
    '''
    for d in range(1, 10000):
        if (e * d) % z == 1:
            return d


def decode(cipher, privatekey):
    '''
    Decrpted Function
    '''
    m = []
    for i in cipher:
        j = (i**privatekey) % n
        m.append(chr(int(j)))
    return m


# Public Key
n = 143
e = 17

# Encrypted Message:
c = [138, 54, 114, 89, 79, 95, 54, 88, 89, 39, 11, 117, 43]

# Main
s = list(find_prime(n))
if check_primes(s[0]) == 1:
    if check_primes(s[1]) == 1:
        z = (int(s[0]) - 1) * (int(s[1]) - 1)
        d = find_d(e, z)
        m = decode(c, d)
        print(''.join(m))
    else:
        print('q in not a prime')
else:
    print('p is not a prime')
