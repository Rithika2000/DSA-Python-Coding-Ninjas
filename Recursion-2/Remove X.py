"""
Given a string, compute recursively a new string where all 'x' chars have been removed.
"""

def removeX(string): 
    if len(string) == 0:
        return string
    else:
        smalloutp = removeX(string[1:])
        if string[0] == 'x':
            return smalloutp
        else:
            return string[0] + smalloutp

# Main
string = input()
print(removeX(string))
