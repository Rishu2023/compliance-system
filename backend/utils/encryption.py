from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(32)  # AES-256 key (32 bytes)
iv = os.urandom(16)   # Initialization vector

def encrypt_data(data: bytes) -> bytes:
    """Encrypt data using AES-256 in CBC mode."""
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_data = data + b" " * (16 - len(data) % 16)  # Pad to block size
    return encryptor.update(padded_data) + encryptor.finalize()