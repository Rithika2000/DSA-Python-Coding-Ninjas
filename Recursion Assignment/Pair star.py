"""
Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
"""

def Pair(S):
    if len(S) == 1:
        return S
    smalloutp = Pair(S[1:])
    if S[0] == S[1]:
        outp = S[0] + '*' + smalloutp
        return outp
    else:
        return S[0] + smalloutp




S = input()
print(Pair(S))
