# Write a Python program to count the frequency of words in a file. 

file = open("10_ques.txt","r")
file_list = file.read().split()
# print(file_list)
word_dict = {}

for i in file_list:
    if i in word_dict:
        word_dict[i] = word_dict[i] + 1
    else:
        word_dict[i] = 1
print(word_dict)
file.close()