import os
import uuid

def generate_unique_filename(instance,filename):
    exe = filename.split(".")[-1]
    new_filename = f'{str(uuid.uuid4())}_{instance.SUFFIX_WORD}.{exe}'

    return os.path.join(instance.DIR_NAME,new_filename)

"""
class Instance:
    def __init__(self, dir_name, suffix_word):
        self.DIR_NAME = dir_name
        self.SUFFIX_WORD = suffix_word

def generate_unique_filename(instance,filename):
    exe = filename.split(".")[-1]
    # DIR_NAME = 'employee_profile'
    # SUFFIX_WORD = 'empProfile'
    new_filename = f'{str(uuid.uuid4())}_{instance.SUFFIX_WORD}.{exe}'

    return os.path.join(instance.DIR_NAME,new_filename)

DIR_NAME = 'employee_profile'
SUFFIX_WORD = 'empProfile'
filename = 'example.jpg'
instance = Instance('employee_profile','empProfile')
print(generate_unique_filename(instance,filename))
"""