def sorting(numbers):
    n=len(numbers)
    for i in range(n):
        for j in range(0,n-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return numbers         
print(sorting([12,73,98,21,4,43]))
