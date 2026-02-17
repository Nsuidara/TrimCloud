import hashlib
import random
import string


def generate_code(value: str, length: int = 6) -> str:
    if not isinstance(value, str):
        raise TypeError("value must be str")
    if not isinstance(length, int):
        raise TypeError("length must be int")

    salt = "".join(random.choices(string.ascii_letters + string.digits, k=5))
    hash_object = hashlib.sha256((value + salt).encode())
    return hash_object.hexdigest()[:length]
