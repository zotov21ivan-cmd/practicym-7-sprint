import string
import random

def generate_random_string(self, length: int, charset: str = string.ascii_letters) -> str:
    return ''.join(random.choices(charset, k=length))