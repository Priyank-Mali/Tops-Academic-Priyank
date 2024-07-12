# •	Write python program that user to enter only odd numbers, else will raise an exception

   
while True:
    try:
        num = int(input("Enter number: "))
        if num % 2 != 0:
            print("You entered:", num)
        else:
            raise ValueError("Entered number is even. Please enter only odd numbers.")
    except ValueError as ve:
        print(type(ve).__name__+": Enter only integers")
