# How Do You Traverse Through A Dictionary Object In Python? 

my_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

for i in my_dict:
    # print(i)             # this print key of my dict
    print(my_dict[i])    # this print value at that key

for key,value in my_dict.items():
    print(key,"->",value)

for key in my_dict.keys():
    print(key,":",my_dict[key])