# Instead of writing it ourselves, let's use a pre-written one from PyCrypto
# PyCrypto is the library we'll be using for the project

# To start with, let's import the XOR cipher
from Cryptodome.Cipher import XOR
# We'll also use their random to get random bits for our key
from Cryptodome.Random import get_random_bytes

m = "Jerry Seinfeld will be chosen to star in the new Microsoft commercial".encode(
    "ascii")
key = get_random_bytes(16)

print(m)

# Create a new cipher object and pass in the key to be used
# For PyCrypto, the key must be between 1 and 32 bytes -- likely to discourage real world usage
cipher = XOR.new(key)
c = cipher.encrypt(m)
print(c)

# We need to reset the cipher as, by default, the cipher would continue from where it left off
# (i.e. it assumes you're going to continue encrypting or decrypting)
cipher = XOR.new(key)
m_dash = cipher.decrypt(c)
print(m_dash)
