#########
## Hashing

# Import the hash functions from the crypto library we'll be using, PyCrypto
# For more details: https://www.dlitz.net/software/pycrypto/api/current/Crypto.Hash-module.html
from Cryptodome.Hash import MD5, SHA256, SHA512

print("Let's introduce you to some simple hashing using the PyCrypto library")
print("=-=-=" * 5)

# First we select the message we want to encode -- in this case the letter "a"
msg = "My secret message"
# All strings in Python 3 are Unicode by default
# The hash functions expect to work only on bytes, so we need convert it to ASCII
# This can be done by either encoding the message:
msg = msg.encode("ascii")
# or by initialising the string with a "b" infront of it, indiciating it's a byte string
msg = b"My secret message"
# or by using the bytes converter
msg = bytes("My secret message", "ascii")

print("We'll hash the string %s" % msg)

print("MD5    Hexdigest (128 bit):")
print(MD5.new(msg).hexdigest())
print("SHA256 Hexdigest (256 bit):")
print(SHA256.new(msg).hexdigest())
print("SHA512 Hexdigest (512 bit):")
print(SHA512.new(msg).hexdigest())
print()

print()
# This will pause the console on Windows machines so that the output can be read
input("End of task -- press Enter")
