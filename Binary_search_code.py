<<<<<<< HEAD
def binarysearch(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1       
if __name__=='__main__':
    arr=[2,3,45,7,87,43,5]
    x=43
    result=binarysearch(arr,x)
    if result!=-1:
        print("elements present in the index",result)
    else:
        print("element is not present")
 
    
=======
def binarysearch(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1       
if __name__=='__main__':
    arr=[2,3,45,7,87,43,5]
    x=43
    result=binarysearch(arr,x)
    if result!=-1:
        print("elements present in the index",result)
    else:
        print("element is not present")
 
    
>>>>>>> 43d0729283787bdad5828806f7eb7bed97c4c756
