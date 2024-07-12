# •	When is the finally block executed? 
# -> always executed 

def divide():
    while True:
        try:
            num1 = int(input("Enter number1: "))
            num2 = int(input("Enter number2: "))
            res = num1/num2
        except Exception as e:
            print(type(e).__name__)
        else:
            print(res)
        finally:
            print("Successfully done!!")

divide()
