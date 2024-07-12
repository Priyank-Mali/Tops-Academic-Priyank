 
# Write a Python program to count the occurrences of each word in a given sentence.

input_str = "Write a Python program to count the occurrences of each word in A given sentence"
str_to_list = input_str.lower().split()
# print(take_list)

emp_list = []
count_word = []
for word in str_to_list:
    if word not in emp_list:
        emp_list.append(word)
        count_word.append([word,str_to_list.count(word)])
print(count_word)    


#______________________________________________________________________________________________
# WAP to count each chracter in string

input_str = "Write a Python program to count the occurrences of each word in a given sentence".lower()

emp_list = []
count_chr = []
for chr in input_str:
    if chr not in emp_list:
        emp_list.append(chr)
        count_chr.append((chr,input_str.count(chr)))
print(count_chr)