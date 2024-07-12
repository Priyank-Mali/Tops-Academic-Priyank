# •	Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

while(1):
    try:
        number = int(input("Enter the number: "))
        if number%2==0:
            print(f"{number} is Even number !!")
        else:
            print(f"{number} is Odd number !!")
        more_check = input("Do you want more number chech?)y/n: ").lower()
        if more_check!='y':
            break
        
    except ValueError:
        print("Please enter valid number !!")
        continue