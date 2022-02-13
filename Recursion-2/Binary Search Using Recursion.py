def binarySeach(a,x,si,ei):
    if si>ei:
        return -1
    
    mid = (si+ei)//2
    if a[mid]==x:
        return mid
    
    elif a[mid]>x:
        return binarySeach(a,x,si,mid-1)
    else:
        return binarySeach(a,x,mid+1,ei)

binarySeach([1,3,4,5,6,7,8,9,11],5,0,8)

