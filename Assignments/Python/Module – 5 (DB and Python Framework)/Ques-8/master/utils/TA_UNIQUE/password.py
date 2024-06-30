import string
import random

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for char in range(length):
        password += random.choice(characters)
    return password
