def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped==False:
            break
    return arr
mylist=[65,87,43,21,98,21,1,5,2,6]
result=bubble(mylist)
print("sortedlist:",result)
