"""

Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Output Format :Sum

"""


def sumArray(arr):
    # Please add your code here)
    m=len(arr)
    if len(arr)==0:
        return 0
    else:
        num = arr[1:]
        smalloutp = sumArray(num)
        outp = arr[0] + smalloutp
        return outp
    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
