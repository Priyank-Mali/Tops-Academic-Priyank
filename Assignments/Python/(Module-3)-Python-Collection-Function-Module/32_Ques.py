# Write a Python script to sort (ascending and descending) a dictionary by value. 

my_dict = {
    1:99,
    0:90,
    2:81
}

# sort by keys:
new_dict = sorted(my_dict.items(),key = lambda x : x[0])
print(new_dict)

# sort by value:
new_dict = sorted(my_dict.items(),key = lambda x : x[1])
print(new_dict)
