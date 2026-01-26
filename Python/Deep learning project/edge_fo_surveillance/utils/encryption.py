from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def generate_key():
    """
    Generates a 256-bit AES key
    """
    return AESGCM.generate_key(bit_length=256)

def encrypt_data(data_bytes, key):
    """
    Encrypts data using AES-GCM
    Returns: nonce, ciphertext
    """
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # 96-bit nonce
    ciphertext = aesgcm.encrypt(nonce, data_bytes, None)
    return nonce, ciphertext

def decrypt_data(nonce, ciphertext, key):
    """
    Decrypts AES-GCM encrypted data
    """
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext
