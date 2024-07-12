# Write a Python program to get the Factorial number of given number.

while(True):

    num = int(input("Enter the number: "))
    if num<0:
        print("Please enter positive number !!")
        continue

    fact = 1
    for i in range(1,num+1) :
        fact = fact * i
        
    print(f"factorial of {num} is: ",fact)
    more_fact = input("Do want more results?(y/n): ").lower()
    if more_fact!='y':
        break

