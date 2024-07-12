# Write a Python function that takes two lists and returns true if they have at least one common member. 

def compare(list1,list2):
    flag = False
    for i in list1:
        for j in list2:
            if i==j:
                flag = True
                break
    if flag:
        print("both list have some common factor")
    else:
        print("both list have nothing to common")


list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [10,11,12,13,14,15,16]
list3 = ["priyank","mali","rajesh"]
list4 = ["rahul","ramesh","mahesh"]
compare(list1,list2)
compare(list3,list4)
