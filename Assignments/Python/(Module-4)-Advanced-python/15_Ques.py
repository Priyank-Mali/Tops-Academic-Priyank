# •	When will the else part of try-except-else be executed? 
'''
try:
    # can be error / not error
except <error type>:
    # execute if the try block throws error
else:
    # do this if try block executes successfully withoout errors
'''

try:
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    res = num1/num2
except Exception as e:
    print("Error: ",type(e).__name__)
else:
    print(res)

