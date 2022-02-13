"""
Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
"""

def Countzero(N):
    if N==0:
        return 1
    if N==1:
        return 0
    if N//10 == 0:
        return 0
    smalloutp = Countzero(N//10)
    if N%10 == 0:
        return 1+smalloutp
    else:
        return smalloutp











N = int(input())
print(Countzero(N))
