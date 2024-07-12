# Write a Python program to reverse a tuple

input_tuple = input("Enter eny element seprated by comma: ").split(",")

print(f"Your Original Tuple is: {tuple(input_tuple)}")

print(f"Your reverse Tuple is: {tuple(input_tuple[::-1])}")