# Let's create a simple XOR cipher
m = "DNA test results: Luke Skywalker and Darth Vader are related".encode(
    "ascii")
key = "darth123".encode("ascii")
print("Encoding m =", m)


def xor_bytes(m, k):
    c = []
    for i in range(len(m)):
        # For each letter in the message, we xor it with the value from the key
        # The key's value uses modulus to repeat the key and use the letters in the appropriate spot
        c.append(m[i] ^ key[i % len(k)])
    return c


# Notice that to encrypt and decrypt it's the exact same operation
c = xor_bytes(m, key)
print("c =", c)
m_dash = xor_bytes(c, key)

# We tell Python to read the block of bytes as a string instead of raw numbers
m_dash = bytes(m_dash).decode("ascii")
print("Reconstructed message m =", m_dash)
