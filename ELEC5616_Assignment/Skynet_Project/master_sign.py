import os
from Cryptodome import Random
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from Cryptodome.Signature import PKCS1_PSS


def generate_keys():
    # RSA algorithm
    key = RSA.generate(4096)
    # Generate private key
    private_pem = key.exportKey(pkcs=8)
    # Generate public key
    public_pem = key.publickey().exportKey()
    # Create file for keys and write it in binary
    with open('master_public.pem', 'wb') as f:
        f.write(public_pem)
    with open('master_private.pem', 'wb') as f:
        f.write(private_pem)


def sign_file(fi):
    # Read private key file in binary
    with open("master_private.pem", 'rb') as f:
        private_key = RSA.importKey(f.read())
    # Generate nonce
    nonce = str(Random.random.StrongRandom().getrandbits(20)).encode()
    # Hash the file
    hash_file = SHA256.new(fi)
    # RSA signature by using private key
    signature = PKCS1_PSS.new(private_key).sign(hash_file)
    return nonce + signature + fi


if __name__ == "__main__":
    # generate_keys()
    fn = input("Which file in pastebot.net should be signed? ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        os._exit(1)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    signed_f = sign_file(f)
    signed_fn = os.path.join("pastebot.net", fn + ".signed")
    out = open(signed_fn, "wb")
    out.write(signed_f)
    out.close()
    print("Signed file written to", signed_fn)
