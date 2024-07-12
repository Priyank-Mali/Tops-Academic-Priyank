# •	Write a Python function to reverses a string if its length is a multiple of 4. 

input_str = input("Enter a string: ")

# rev_str = input_str[::-1]

if len(input_str)%4==0:
    rev_str = input_str[::-1]
    print(rev_str)
else:
    print("String length is not multiple of 4")
