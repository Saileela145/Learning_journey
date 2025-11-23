def merge(a,b):
    merged=[]
    for x in a:
        merged.append(x)
    for y in b:
        merged.append(y)
    return merged
print(merge([1,4,6,5],[7,9]))
