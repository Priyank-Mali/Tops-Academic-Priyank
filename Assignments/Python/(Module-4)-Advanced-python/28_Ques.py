# •	What relationship is appropriate for Course and Faculty? 

'''
Has a relationship (composition)
->This implies that a Course class would contain an instance of a Faculty class.
'''

class Faculty:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty

math_professor = Faculty("priyank")
math_course = Course("Mathematics", math_professor)

print(math_course.name)       
print(math_course.faculty.name)  