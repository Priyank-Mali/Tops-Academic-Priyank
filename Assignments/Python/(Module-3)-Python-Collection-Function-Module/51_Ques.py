# Write a Python function that checks whether a passed string is palindrome or not 


def Palindrome(str):
    rev_str = str[::-1]
    if rev_str == str:
        return "Palindrome"
    else:
        return "Not Palindrome"

input_str = input("Enter eny string: ")
print(Palindrome(input_str))