# •	Can one block of except statements handle multiple exception? 

try:
    res = 10/0
    print(x)
except (ZeroDivisionError,NameError):
    print("Error: Something is wrong!!")
except Exception as e:
    print("Error: ",e)
