"""
Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:

a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'

If all the rules are followed by the given string, return true otherwise return false.

"""

def AB(s):
    if len(s) == 0:
        return 'true'
    
    if len(s) == 1:
        if s[0] == 'a':
            return 'true'
        else:
            return 'false'
    
    if len(s) ==2:
        if s[0] == 'a' and s[1] == 'a':
            return 'true'
        else:
            return 'false'
    
    if len(s)>2:
        if s[0] == 'a' and s[1] == 'b' and s[2] =='b':  #induction hypothesis
            smallresult = AB(s[3:])
        elif s[0] == "a" and s[1] == "a":
            smallresult = AB(s[1:])
        else:
            return 'false'
        return smallresult





S = input()
print(AB(S))


