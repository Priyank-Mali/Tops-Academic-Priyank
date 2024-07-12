# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

my_list = """
Write a Python program to count the number of strings 
where the string length is 2 or more and the first and 
last character are same from a given list of strings""".split(" ")

count = 0
i = 0
firstlast = 0
firstlast_word = []
for word in my_list:
    if len(word)>2:
        count = count + 1
        
    if len(word)>1 and word[i]==word[len(word)-1]:
        firstlast += 1
        firstlast_word.append(word)

print(f"There are {firstlast} words whoose first and last letter is same and the words are {firstlast_word}")
print(f"There are {count} words whose length is more than 2")