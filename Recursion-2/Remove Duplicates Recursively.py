"""
Given a string S, remove consecutive duplicates from it recursively.
"""

def removeConsecutiveDuplicates(string):
    if len(string)==0 or len(string)==1:
        return string
    if string[0]==string[1]:
        secondbox=removeConsecutiveDuplicates(string[1:])
        return secondbox
    else:
        secondbox=string[0]+removeConsecutiveDuplicates(string[1:])
        return secondbox
    # Please add your code here
    pass
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
