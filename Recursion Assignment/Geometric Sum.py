"""
Given k, find the geometric sum i.e.

1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 

using recursion.

"""

def Gsum(k):
    if k==0:
        return 1
    return 1/2**k + Gsum(k-1)

k = int(input())
print (str.format('{0:.5f}',Gsum(k)))

