# Write a Python function to check whether a number is in a given range 

def checkNum(start,end,num):
    if num in range(start,end+1):
        return f"{num} is present in range"
    else:
        return f"{num} is not present in range"


startRange = int(input("Enter starting range: "))
endRange = int(input("Enter ending range: "))
inputNum = int(input("Enter number: "))

print(checkNum(startRange,endRange,inputNum))