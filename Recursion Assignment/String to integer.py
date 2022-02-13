"""
Write a recursive function to convert a given string into the number it represents. 
That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.
"""

def str_to_num(str):
    l=len(str)
    if l==0 or l==1:
        return str
    small=str_to_num(str[1:])
    return int(str[0])*10**(l-1)+int(small)




N = input()
print(str_to_num(N))
