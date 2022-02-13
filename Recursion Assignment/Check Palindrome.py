"""
Check whether a given String S is a palindrome using recursion. Return true or false.
"""

def palindrome(str):
    if len(str) <= 1:
        return 'true'
    
    if str[0] == str[len(str)-1]:
        smalloutp = palindrome(str[1:len(str)-1])
        return smalloutp
    else:
        return 'false'






str = input()
'''if palindrome(str) == True:
    print('true')
else:
    print('false')'''
print(palindrome(str))
