def selection(arr,size):
    for i in range(size):
        minvalue=i
        for j in range(i+1,size):
            if arr[j]<arr[minvalue]:
               minvalue=j
        arr[i],arr[minvalue]=arr[minvalue],arr[i]
    return arr
mylist=[65,2,21,7,3,98,22,87,-45,-3,-9]
size=len(mylist)
result=selection(mylist,size)
print(result)
