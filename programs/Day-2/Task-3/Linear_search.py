def linear_search(num,target):
    for i in range(len(num)):
        if num[i]==target:
            return i
    return -1
print(linear_search([10,20,98,67,54],67))
