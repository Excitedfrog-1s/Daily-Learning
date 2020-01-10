import os
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA

def decrypt_valuables(f):
    iv = f[:AES.block_size]
    session_key_encrpyted = f[AES.block_size:(AES.block_size + 256)]
    data_encrypted = f[(AES.block_size + 256):]
    with open('master_private.pem', 'rb') as f:
        private_key = RSA.importKey(f.read())
    session_key = PKCS1_OAEP.new(private_key).decrypt(session_key_encrpyted)
    data = AES.new(session_key, AES.MODE_CFB, iv).decrypt(data_encrypted)
    decode_text = str(data, 'ascii')
    print(decode_text)


if __name__ == "__main__":
    fn = input(
        "Which file in pastebot.net does the botnet master want to view? ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        os._exit(1)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    decrypt_valuables(f)
