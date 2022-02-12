def factorial(n):
    if n == 0 :
        return 1
    smallOutput = factorial(n-1)  #intermediate step
    output = smallOutput * n
    return output

result = factorial(6)



def factWithoutRecursion(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i 
    return fact

result = factWithoutRecursion(100000)
