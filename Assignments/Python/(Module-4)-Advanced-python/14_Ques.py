# How many except statements can a try-except block have? Name Some built-in exception classes:

try:
    # x = 10/0
    inputy = int(input("Enter Number: "))
except ZeroDivisionError:
    print('Error: Division by zero')
except ValueError:
    print('Error: Invalid Value')
except Exception as e:
    print('somthig was wrong',e)

"""
-> ZeroDivisionError
-> ValueError
-> TypeError
-> IndexError
-> FileNotFoundError
-> NameError

"""

