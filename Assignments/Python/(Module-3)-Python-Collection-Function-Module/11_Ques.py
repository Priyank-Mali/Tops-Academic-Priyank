# Write a Python function that takes a list and returns a new list with unique elements of the first list. 

def removeDuplicate(list):
    new_list = []
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i] not in new_list:
                new_list.append(list[i])
    return print(new_list)


my_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

removeDuplicate(my_list)

