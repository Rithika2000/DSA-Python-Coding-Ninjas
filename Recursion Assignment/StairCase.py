"""
A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up to the stairs.
You need to return number of possible ways W.
"""

def StairCase(N):
    if N==1:
        return 1
    if N==2:
        return 2
    if N==3:
        return 4
    outp = StairCase(N-1) + StairCase(N-2)+StairCase(N-3)
    return outp




N = int(input())
print(StairCase(N))
