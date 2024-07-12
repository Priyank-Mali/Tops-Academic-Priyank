# How Do You Check The Presence Of A Key In A Dictionary? 

my_dict = {
    1 : 99,
    2 : 88,
    3 : 77,
    4 : 66
}

inputKey = int(input("Enter any value: "))

if inputKey in my_dict:
    print(f"{inputKey} key is exists in dictionary.")
else:
    print(f"{inputKey} key is not exists in dictionary.")