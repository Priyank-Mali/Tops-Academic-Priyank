import os
import uuid

def generate_unique_filename(instance,filename):
    extansion = filename.split(".")[-1]
    new_filename = f'{str(uuid.uuid4())}_{instance.SUFFIX_WORD}.{extansion}'

    return os.path.join(instance.DIR_NAME,new_filename)

