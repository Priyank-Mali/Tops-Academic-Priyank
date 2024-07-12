# Write a Python script to concatenate following dictionaries to create a new one. 

dict1 = {
    "apple": 2,
    "banana":4
}

dict2 = {
    "mango":6,
    "banana": 4
}

# new_dict = dict1 | dict2

new_dict = dict2
new_dict.update(dict1)

print(new_dict)