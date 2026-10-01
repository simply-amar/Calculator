import sys
import math
import operator
from functools import reduce
from functions import *

print("Welcome to my calculator")

operation = input("[A] for addition,[S] for subtraction, [M] multiplication, [D] division: ")
iterations = int(input("How many numbers you want to operate: ")) #Record the number of number the user wants to operate

if iterations == 1:
    print("Can't operate a single number. Run the program again")
    sys.exit(0)
        
    
nums=[]#Empty list for adding numbers to it

for num in range(0,iterations): #Gets the number from user and append to the empty list
    numb= int(input("Enter your number: "))
    nums.append(numb)
    
# def add(nums):
#     return sum(nums)
# def sub(first,rest):
#     return first-sum(rest)
# def prod(nums):
#     return math.prod(nums)
# def div(nums):
#     return reduce(operator.truediv,nums)
    

if operation.lower() == 'a':
    print(add(nums))
elif operation.lower() == 's':
    print(sub(nums[0],nums[1:]))
elif operation.lower() == 'm':
    print(prod(nums))
else:
    print(div(nums))