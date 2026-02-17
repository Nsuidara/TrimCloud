import hashlib
import random
import string

def generate_code(value, length=6):
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    hash_object = hashlib.sha256((value + salt).encode())
    return hash_object.hexdigest()[:length]