def binary(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        mvalue=arr[mid]
        if mvalue==target:
            return mid
        elif target<mvalue:
            high=mid-1
        else:
            low=mid+1
    return -1
