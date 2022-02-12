def print_1_to_n(n):
    if n == 0 :
        return 
    print_1_to_n(n-1)  # induction step
    print(n)
    return 


print_1_to_n(5)



def print_n_to_1(n):
    if n == 0 :   #base case
        return 
    print(n)
    smalloutput = print_n_to_1(n-1) #induction step
    return smalloutput

print_n_to_1(10)
