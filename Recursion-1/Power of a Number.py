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
