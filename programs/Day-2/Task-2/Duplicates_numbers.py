def f_duplicates(numbers):
    duplicates=[]
    know=[]
    for n in numbers:
        if n in know and n not in duplicates:
            duplicates.append(n)
        else:
            know.append(n)
    return duplicates
print(f_duplicates([1,2,3,4,5,2,3,5,3,6]))
            
        
