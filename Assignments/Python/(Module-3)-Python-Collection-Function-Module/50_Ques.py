# Write a Python function to check whether a number is perfect or not. 

emp_list = []
def perfectNum(num):
    for i in range(1,num+1//2):
        if num%i == 0:
            emp_list.append(i)
    sum = 0
    for i in emp_list:
        sum = sum + i
    
    if sum == num:
        return f"{num} is a perfect number."
    else:
        return f"{num} is not a perfect number."

input_num = int(input("Enter a number: "))
print(perfectNum(input_num))



