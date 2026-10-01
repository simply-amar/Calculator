import math
import operator
from functools import reduce

def add(nums):
    return sum(nums)
def sub(first,rest):
    return first-sum(rest)
def prod(nums):
    return math.prod(nums)
def div(nums):
    return reduce(operator.truediv,nums)