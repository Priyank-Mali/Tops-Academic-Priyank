import string
import random

def generate_random_password(length=8):
   
    chars = string.ascii_letters + string.digits + "@_."
    password = ""
    for ch in range(length):
        password += chars[random.randrange(len(chars))]
    
    return password

