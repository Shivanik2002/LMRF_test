import functools
import operator

list = [1,3,4,5,6,7]
print("the sum of the list element is: ",end=" ")
print(functools.reduce(operator.add,list))

print("________________________________________________")

print("the product of list elements is: ",end=" ")
print(functools.reduce(operator.mul,list))

from functools import reduce
numbers = [11,22,32,45,67,89]

def addition(a,b):
    result = a+b
    return result

print(reduce(addition,numbers,29))    