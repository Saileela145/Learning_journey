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
mylist=[32,4,76,21,87,43,1,8,43,36]
mylist.sort()
targetvalue=8
index=binary(mylist,targetvalue)
if index!=-1:
    print(f"the {targetvalue} is in the index {index}")
else:
    print("the target not found")
