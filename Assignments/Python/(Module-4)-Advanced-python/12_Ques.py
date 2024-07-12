# •	Write a Python program to copy the contents of a file to another file. 


try:
    with open('11_ques.txt','r') as file:
        content = file.read()
    with open('12_ques.txt','w') as file2:
        file2.write(content)
    print('file copied successfully')
except FileNotFoundError:
    print('file not exists')
