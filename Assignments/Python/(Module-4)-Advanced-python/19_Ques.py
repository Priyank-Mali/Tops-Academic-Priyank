# •	How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets. 

while True:
    try:
        num1 = int(input("Enter Number1: "))
        num2 = int(input("Enter Number2: "))
        res = num1/num2
    except ZeroDivisionError as e:
        print(type(e).__name__ +": Number2 cant't be Zero")
    except ValueError as e:
        print(type(e).__name__+": Only Integers values are allow")
    else:
        print("Division: ",res)
    finally:
        print("finally")

