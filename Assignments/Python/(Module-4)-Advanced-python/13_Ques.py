# Explain Exception handling? What is an Error in Python?
'''
-> Exception handling allows you to gracefully handle errors in your python code.
-> preventing crashes and providing fallback mechanism to deal with unexpected errors.

1.) syntax error :

    print(5

2.) runtime error :

    print(5/0) -> ZeroDivisionError
    with open('99_ques.txt','r') as file:  -> FileNotFountError
        file.read()
       
3.) Logical Error : 

    def add(a,b):
        return a-b 
'''

# try:
#     # cose to run
# except:
#     # handle error
