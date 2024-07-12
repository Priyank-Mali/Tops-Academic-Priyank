# Write a Python program to write a list to a file. 

my_list = [
    {'name': 'priyank',
     'age' : 99,
     'contact' : 123456},
     {'name': 'kalam',
      'age' : 88,
      'contact' : 987654}
]

file = open('11_ques.txt','w')
for i in my_list:
    file.write(str(i) + '\n')
file.close()