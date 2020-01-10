# Instead of writing it ourselves, let's use a pre-written one from PyCrypto
# PyCrypto is the library we'll be using for the project

# To start with, let's import the XOR cipher
from Cryptodome.Cipher import DES
# We'll also use their random to get random bits for our key
from Cryptodome.Random import get_random_bytes
# We need to pad the message before encryption
from crypto_utils import ANSI_X923_pad, ANSI_X923_unpad

m = "Jerry Seinfeld will be chosen to star in the new Microsoft commercial".encode(
    "ascii")
key = get_random_bytes(DES.block_size)
print(m)

padded_m = ANSI_X923_pad(m, DES.block_size)

# Create a new cipher object and pass in the key to be used
# For PyCrypto, the key must be between 1 and 32 bytes -- likely to discourage real world usage
cipher = DES.new(key)
c = cipher.encrypt(padded_m)
print(c)

# We need to reset the cipher as, by default, the cipher would continue from where it left off
# (i.e. it assumes you're going to continue encrypting or decrypting)
padded_m = cipher.decrypt(c)
m_dash = ANSI_X923_unpad(padded_m, DES.block_size)
print(m_dash)

# We'll make sure the decrypted message is the same as the original
if m == m_dash:
    print('True')
