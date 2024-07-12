# Write a Python program to returns sum of all divisors of a number 

def sum_allDivisor(num):
    divisor_list = []
    for i in range(1,num+1):
        if num%i==0:
            divisor_list.append(i)
    sum = 0
    for i in divisor_list:
        sum = sum + i
    return sum

inputNumber = int(input("Enter any number: "))
print(f"The sum of all divisor of number {inputNumber} is: {sum_allDivisor(inputNumber)}")
