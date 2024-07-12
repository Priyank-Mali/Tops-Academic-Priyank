"""
How will you compare two lists? 
"""

list1 = [1,2,3]
list2 = [1,1,3]
i = 0
j = 0
if len(list1)!=len(list2):
    print("Both list is Different")
else:
    while i<len(list1) or j<len(list2):
        if list1[i]==list2[j]:
            flag = True
        else:
            flag = False
            break
        i = i + 1
        j = j + 1
    if flag:
        print("Both list is same")
    else:
        print("Length is same but elements are different")


