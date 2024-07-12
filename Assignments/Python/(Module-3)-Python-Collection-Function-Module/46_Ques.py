# Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] 
# Expected Output: Counter ({'item1': 1150, 'item2': 300}) 


my_list =  [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}] 

emp_dict = {}

for i in my_list:
    item = i['item']
    amount = i['amount']
    # print(item)
    # print(amount)
    if item in emp_dict:
        emp_dict[item] = emp_dict[item] + amount
    else:
        emp_dict[item] = amount
print(emp_dict)

