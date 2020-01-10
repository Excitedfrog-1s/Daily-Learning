'''
Optimize notes (After Canvas Message):
1. Change the r(nonce) to both letter and number
2. Add run time calculation
This may take a VERY LONG time (Up to 8 hours in my laptop) to calculate...
'''

import hashlib
import time
import random
import string


def __find_nonce():
    '''
    Generate a random number "r"
    '''
    r = ''.join(
        random.choice(string.digits + string.ascii_letters) for i in range(12))
    return r


def __generate_hash(a):
    '''
    Generate hash value of sentence "a"
    I code this on Python3.7 and it has a error if I not encode it to UTF-8 firstly
    But it also test OK on Python2. Thus, I keep "utf-8" in this code.
    '''
    h = hashlib.sha256(a.encode("utf-8")).hexdigest()
    return h


# Main
start_time = time.time()
a = 'My name is Liyang Han and I love COMP9121!'
while True:
    r = __find_nonce()
    a = a + r
    h = __generate_hash(a)

    # Show the process which looks cool
    print(h)

    # Check if the hash value is starting with 000000
    if h.startswith('000000'):
        print('Magic Sentence Is Found!!!')

        # Show the magic number
        print('The Magic Number is:' + r)

        # Show the final hash
        print('The Hash is:' + h)

        # Abort the circulation
        break

end_time = time.time()

# Calculate the process time
time = end_time - start_time
print('Run Time is:' + time)
