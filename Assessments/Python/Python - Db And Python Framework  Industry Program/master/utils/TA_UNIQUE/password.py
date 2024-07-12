import string
import random

def generate_password(length=8):

    chars = string.ascii_letters + string.digits
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

# print(generate_password())
