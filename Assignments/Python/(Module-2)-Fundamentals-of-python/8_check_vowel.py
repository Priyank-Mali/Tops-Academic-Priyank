# •	Write a Python program to test whether a passed letter is a vowel or not.
while(1):
        chars = (input("Enter Character: ")).lower()

        if chars == 'a' or chars == 'e' or chars == 'i' or chars == 'o' or chars == 'u' :
            print("Vowel !!")
        else:
            print("Consonants") 
        more_char = input("Want more check?(y/n): ").lower()
        if more_char!='y':
            break