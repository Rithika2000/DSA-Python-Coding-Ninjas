def isSorted(arr,si):
    l = len(arr)
    if si == l-1 or si == l:   # si = l-1 depicts last element of the list and si==l means no element
        return True 
    
    if arr[si] > arr[si+1]:
        return False
    
    isSortedRemaningList = isSorted(arr,si+1)
    return isSortedRemaningList


arr = [1,2,3,4,1,12]
isSorted(arr,0)
