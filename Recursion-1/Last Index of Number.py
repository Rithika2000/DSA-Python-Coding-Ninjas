"""

Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0.

"""

def lastIndex(arr,x,li):
    l=len(arr)
    if li==-1:
        return -1
    if arr[li] == x:
        return li
    else:
        smalloutp = lastIndex(arr,x,li-1)
        return smalloutp



n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(arr, x,n-1))
