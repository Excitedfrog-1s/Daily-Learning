#########
## HMACs

# For more details: https://www.dlitz.net/software/pycrypto/api/current/Crypto.Hash.HMAC-module.html
from Cryptodome.Hash import HMAC
from Cryptodome.Hash import SHA256

print("Now let's perform message authentication using HMAC")
print("=-=-=" * 5)

secret = "Batman's Secret for Gordon".encode("ascii")
msg = "Batman, meet me in the alley behind Arkham Asylum. Commission Gordon.".encode(
    "ascii")
mac = "bb46120970e71e1d63253a124c19ed4bd7f4268410f4e57e637d66f82d30ac3e"
# mac = "000ef9a895a63ffa484e0dded9410978721782aec8c4a68f467357ce03a4af0cea52f7997474b14708b6be434ac4152afb7740395d2ed41b6578a37acc644a5c"

print(
    "Batman received a message supposedly from Commissioner Gordon, which says:"
)
print(msg)
print("It came with a MAC: %s" % mac)

# The HMAC module uses MD5 by default, but we can specify another hash function
# In general, MD5 should not be used for any new security applications as it has numerous issues
hmac = HMAC.new(secret, digestmod=SHA256)


# We add the message in by updating the hash
hmac.update(msg)

# We'll also show that adding the message chunks at a time is equivalent to adding all the message at once
chunked_hmac = HMAC.new(secret, digestmod=SHA256)
chunked_hmac.update("Batman, ".encode("ascii"))
chunked_hmac.update(
    "meet me in the alley behind Arkham Asylum. ".encode("ascii"))
chunked_hmac.update("Commission Gordon.".encode("ascii"))

# We can then compare the hexdigest of each hash
# If they're equal, we know the message has not been modified and the secret key must be the same
if hmac.hexdigest() == chunked_hmac.hexdigest() == mac:
    print("Batman used HMAC and confirmed Gordon's identity")
else:
    print(
        "It was someone trying to pretend it was Gordon... Joker's henchmen perhaps?"
    )

print()
# This will pause the console on Windows machines so that the output can be read
input("End of task -- press Enter")
