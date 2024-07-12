# Write a Python program to check multiple keys exists in a dictionary.

dict1 = {
    "apple":6,
    "banana":7,
    "cherry":9,
    "apple":11
}

key_List = ['apple','mango','cherry','pineaaple']
for key in key_List:
    if key in dict1:
        print(f"{key} key is exists")
    else:
        print(f"{key} key is not exists")

    



