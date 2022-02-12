"""

Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Note : For this question, you can assume that 0 raised to the power of 0 is 1

"""

def exp(a,b):
    if b==1:
        return a
    if b==0:
        return 1
    else:
        SmallOutp = exp(a,b-1)
        outp = SmallOutp * a
        return outp
    
    
    
a, b = input().split()
a = int(a)
b = int(b)
print(exp(a,b))
