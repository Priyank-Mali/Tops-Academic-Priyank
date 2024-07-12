# Write a Python script to check if a given key already exists in a dictionary. 

dict1 = {
    "apple":6,
    "banana":7,
    "cherry":9
}

fruit_input = input("Enter fruit name: ")
fruit_value = int(input("Enter no of fruit: "))

if fruit_input in dict1.keys():
    print("This fruit(key) is already present")
else:
    dict1[fruit_input] = fruit_value
print(dict1)