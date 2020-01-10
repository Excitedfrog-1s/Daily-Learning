import os
from Cryptodome import Random
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Signature import PKCS1_PSS

# Instead of storing files on disk,
# we'll save them in memory for simplicity
filestore = {}
# Valuable data to be sent to the botmaster
valuables = []
# Storage nonces that already used
used_nonce = []


def save_valuable(data):
    valuables.append(data)


def encrypt_for_master(data):
    # Encrypt the file so it can only be read by the bot master
    with open('master_public.pem', 'rb') as f:
        public_key = RSA.importKey(f.read())
    session_key = Random.get_random_bytes(32)
    session_key_encrpyted = PKCS1_OAEP.new(public_key).encrypt(session_key)
    iv = Random.new().read(AES.block_size)
    data_encrypted = AES.new(session_key, AES.MODE_CFB, iv).encrypt(data)
    return iv + session_key_encrpyted + data_encrypted


def upload_valuables_to_pastebot(fn):
    # Encrypt the valuables so only the bot master can read them
    valuable_data = "\n".join(valuables)
    valuable_data = bytes(valuable_data, "ascii")
    encrypted_master = encrypt_for_master(valuable_data)
    # "Upload" it to pastebot (i.e. save in pastebot folder)
    f = open(os.path.join("pastebot.net", fn), "wb")
    f.write(encrypted_master)
    f.close()
    print("Saved valuables to pastebot.net/%s for the botnet master" % fn)


def verify_file(fi):
    '''
    Check nonce first and the verify the signature
    '''
    with open('master_public.pem', 'rb') as f:
        public_key = RSA.importKey(f.read())
    nonce = fi[:6]
    sign = fi[6:518]
    msg = fi[518:]
    hash_msg = SHA256.new(msg)
    if nonce in used_nonce:
        print("Detect Replay Attack!!")
        f.close()
    else:
        used_nonce.append(nonce)
    if PKCS1_PSS.new(public_key).verify(hash_msg, sign):
        return True
    else:
        return False


def process_file(fn, f):
    if verify_file(f):
        # If it was, store it unmodified
        # (so it can be sent to other bots)
        # Decrypt and run the file
        filestore[fn] = f
        print("Stored the received file as %s" % fn)
    else:
        print("The file has not been signed by the botnet master")


def download_from_pastebot(fn):
    # "Download" the file from pastebot.net
    # (i.e. pretend we are and grab it from disk)
    # Open the file as bytes and load into memory
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        return
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    process_file(fn, f)


def p2p_download_file(sconn):
    # Download the file from the other bot
    fn = str(sconn.recv(), "ascii")
    f = sconn.recv()
    print("Receiving %s via P2P" % fn)
    process_file(fn, f)


def p2p_upload_file(sconn, fn):
    # Grab the file and upload it to the other bot
    # You don't need to encrypt it only files signed
    # by the botnet master should be accepted
    # (and your bot shouldn't be able to sign like that!)
    if fn not in filestore:
        print("That file doesn't exist in the botnet's filestore")
        return
    print("Sending %s via P2P" % fn)
    sconn.send(bytes(fn, 'ascii'))
    sconn.send(bytes(filestore[fn]))


def run_file(f):
    # If the file can be run,
    # run the commands
    pass
