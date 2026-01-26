from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def encrypt_data(data):
    key = AESGCM.generate_key(bit_length=128)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data, None)
    return ciphertext
