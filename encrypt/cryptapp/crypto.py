from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_text(key, text):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt_text(key, encrypted_text):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text