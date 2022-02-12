"""

Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
Do this recursively.

"""

def checkNumber(arr, x):
    # Please add your code here
    if len(arr)==0:
        return False
    if arr[0] == x:
        return True
    else:
        num=arr[1:]
        SmallOutp = checkNumber(num,x)
        return SmallOutp

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
