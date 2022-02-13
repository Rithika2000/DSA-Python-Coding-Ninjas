"""
Given two integers M & N, calculate and return their multiplication using recursion. 
You can only use subtraction and addition for your calculation. No other operators are allowed.
"""

from sys import setrecursionlimit
setrecursionlimit(10**6) 

def multi(M,N):
    if M==0 or N==0:
        return 0
    if M==1:
        return N
    if N==1:
        return M
    smalloutp = multi(M,N-1)
    outp = M + smalloutp
    return outp

M = int(input())
N = int(input())
print(multi(M,N))
