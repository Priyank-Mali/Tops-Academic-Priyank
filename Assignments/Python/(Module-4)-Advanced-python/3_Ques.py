# Write a Python program to append text to a file and display the text.

file = open("3_ques.txt",'w')
file.write("python is object oriented programming language") 
file.close()

file = open("3_ques.txt",'a')
file.write("\npython is interpreted programming language")
file.close()