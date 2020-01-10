import struct
import random
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from Cryptodome import Random
from Cryptodome.Hash import HMAC
from dh import create_dh_key, calculate_dh_secret


class StealthConn(object):
    def __init__(self, conn, client=False, server=False, verbose=False):
        self.conn = conn
        self.cipher = None
        self.hmac = None
        self.nonce_list = []
        self.client = client
        self.server = server
        self.verbose = verbose
        self.initiate_session()

    AES.block_size = 16

    def initiate_session(self):
        '''
        Perform the initial connection handshake for agreeing on a shared secret.
        This can be broken into code run just on the server or just on the client.
        All the function want to do here is to ensure the data confidentiality.
        Key: A key used to generate IV. Obtained from shuffled shared hash.
        '''
        if self.server or self.client:
            # DH crete keys
            my_public_key, my_private_key = create_dh_key()
            # Send them our public key
            self.send(bytes(str(my_public_key), "ascii"))
            # Receive their public key
            their_public_key = int(self.recv())
            # Obtain our shared secret
            self.shared_hash = calculate_dh_secret(their_public_key,
                                                   my_private_key)
            print("Shared hash: {}".format(self.shared_hash))
            key = list(self.shared_hash)
            random.shuffle(key)
            # Generate IV
            iv = bytes(str(key).encode()[:AES.block_size])
            # Convert hexstr to byte
            self.shared_hash = bytes.fromhex(self.shared_hash)
            # AES encrypt with CFB mode
            self.cipher = AES.new(self.shared_hash, AES.MODE_CFB, iv)
            self.hmac = HMAC.new(self.shared_hash, None, SHA256.new())

    def send(self, data):
        '''
        Before sending the data, we should ensure:
        1. Nonce: Prevent replay attack
        2. HMAC: Ensure the data integrity
        3. Data Signature: Ensure the data non-repudiation
        '''
        if self.cipher:
            nonce = Random.random.StrongRandom().getrandbits(10)
            # Encrypt nonce and data together
            encrypted_data = self.cipher.encrypt(str(nonce).encode() + data)
            # Update the HMAC
            self.hmac.update(encrypted_data)
            convert_hmac = bytes(self.hmac.hexdigest(), 'ascii')
            encrypted_data = encrypted_data + convert_hmac
            if self.verbose:
                # This 2 lines use in test only!
                # print("Nonce: ", nonce)
                # print("HMAC: {}".format(convert_hmac))
                print("Original data: {}".format(data))
                print("Encrypted data: {}".format(repr(encrypted_data)))
                print("Sending packet of length {}".format(
                    len(encrypted_data)))
        else:
            encrypted_data = data

        # Encode the data's length into an unsigned two byte int ('H')
        pkt_len = struct.pack('H', len(encrypted_data))
        self.conn.sendall(pkt_len)
        self.conn.sendall(encrypted_data)

    def recv(self):
        '''
        Before the reciver accept data, reciver needs to verify 3 things:
        1. HMAC. Calculate the HMAC again and compare. Close connection if not same.
        2. Nonce. Check if the nonce is already in nonce list. Close connection if yes.
        3. Signature. Check if the sender is the really sender. Close connection if not.
        '''
        # Decode the data's length from an unsigned two byte int ('H')
        pkt_len_packed = self.conn.recv(struct.calcsize('H'))
        unpacked_contents = struct.unpack('H', pkt_len_packed)
        pkt_len = unpacked_contents[0]
        encrypted_data = self.conn.recv(pkt_len)
        # Extract original HMAC
        send_hmac = encrypted_data[-64:]
        if self.cipher and self.hmac:
            # Calculate HMAC again
            self.hmac.update(encrypted_data[0:-64])
            recv_hmac = self.hmac.hexdigest().encode()
            # Check HMAC
            if recv_hmac != send_hmac:
                print("Message has been compromised!")
                self.conn.close()
            data = self.cipher.decrypt(encrypted_data[:64])
            # Extract Nonce
            nonce = data[:10]
            # Check Nonce
            if nonce in self.nonce_list:
                print("Detect Replay Attack!")
                self.conn.close()
            else:
                print("Nonce Status OK")
                self.nonce_list.append(nonce)

            if self.verbose:
                print("Receiving packet of length {}".format(pkt_len))
                print("Encrypted data: {}".format(repr(encrypted_data)))
                print("Original data: {}".format(data))
        else:
            data = encrypted_data

        return data

    def close(self):
        self.conn.close()
