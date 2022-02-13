def replacestring(s,a,b):
    l = len(s)
    if len(s) == 0:
        return s
    smalleroutput = replacestring(s[1:],a,b)
    if a[0] == a:
        return b+smalleroutput
    else:
        return s[0]+smalleroutput

replacestring('abab',"a","b")

ef replacepi(s):
    if len(s)==0 or len(s) ==1:
        return s
    
    if s[0]=='p' or s[1]=='i':
        smalloutput=replacepi(s[2:])
        return '3.14'+ smalloutput
    else:
        smalloutput=replacepi(s[1:])
        return s[0]+ smalloutput

replacepi('abcpipipi')

