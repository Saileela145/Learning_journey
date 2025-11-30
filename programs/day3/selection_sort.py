def selection(arr,size):
    for i in range(size):
        minvalue=i
        for j in range(i+1,size):
            if arr[j]<arr[minvalue]:
               minvalue=j
        arr[i],arr[minvalue]=arr[minvalue],arr[i]
    return arr

