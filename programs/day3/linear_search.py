def linear(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1
mylist=[6,32,76,9,2,87,3,65]
target=76
result=linear(mylist,target)
if result!=-1:
    print(f"the {target} value is in index{result}")
else:
    print("target not found")

mylist1=[45,65,9,3,0,67,32,98]
mylist1.sort()
targetvalue=67
result1=linear(mylist1,targetvalue)
if result1!=-1:
   print(f"the {targetvalue} value is in index{result1}")
else:
    print("target not found")
