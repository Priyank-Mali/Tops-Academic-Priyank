# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 

str = "The family, despite facing financial challenges in the past, is now not poor due to their hard work and perseverance."
print("occurrence in string at:",str.find("not"))
print("occurrence in string at:",str.find("poor"))

new_str = str.replace("not poor","good")
print(new_str)