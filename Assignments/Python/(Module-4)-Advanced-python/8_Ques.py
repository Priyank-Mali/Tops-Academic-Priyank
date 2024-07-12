# •	Write a python program to find the longest words. 

file = open("8_ques.txt",'r')
file_list = file.read().split()
max_word = max(file_list,key=len)
print(f"The word is: {max_word} and length of word is:{len(max_word)}")
file.close()
