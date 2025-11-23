def sorting(number):
    n=len(number)
    for i in range(n):
        for j in range(0,n-i-1):
            if number[j]>number[j+1]:
                number[j],number[j+1]=number[j+1],number[j]
    return number         
print(sorting([12,73,98,21,4,43]))
