# Write a Python script to merge two Python dictionaries 

my_dict1 = {
    'apple':6,
    'banana':9,
    'cherry':11
}

my_dict2 = {
    'mango':3,
    'papaya':8,
    'orange':11,
    'cherry':5
}
final_dict = {}

for key,value in my_dict1.items():
    final_dict[key] = value

for key,value in my_dict2.items():
    if key in final_dict:
        final_dict[key] = final_dict[key] + value
    else:
        final_dict[key] = value


print(final_dict)
