import uuid

def generate_unique_id(instance):
    unique_id = f'{str(uuid.uuid4())}-{instance.SUFFIX_WORD}'
    return unique_id


# class Student():
#     def __init__(self,SUFFIX_WORD):
#         self.SUFFIX_WORD = SUFFIX_WORD
        
#     def generate_unique_id(self):
#         unique_id = f'{str(uuid.uuid4())}-{self.SUFFIX_WORD}'
#         return unique_id

# student = Student('STU')
# print(student.generate_unique_id())
