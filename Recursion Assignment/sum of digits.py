"""
Write a recursive function that returns the sum of the digits of a given integer.
"""

def sumdigits(p):
    if len(p) == 1:
        return int(p)
    smalloutp = sumdigits(p[1:])
    outp = int(p[0]) + int(smalloutp)
    return outp









N = int(input())
p = str(N)
print(sumdigits(p))
