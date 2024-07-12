# Write a Python function that takes a list of words and returns the length of the longest one.

input_list =input("Enter a list: ")
str_to_list = input_list.split(" ")

long_word = ""
small_word = ""

long_str = 0
small_str = float("inf")
for word in str_to_list:
    if len(word) > long_str:
        long_str = len(word)
        long_word = word

for word in str_to_list:
    if len(word) < small_str:
        small_str = len(word)
        small_word = word


print("longest word is:",long_word,"and it's length is:",len(long_word))
print("smallest word is:",small_word,"and it's length is:",len(small_word))
