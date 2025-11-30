def second_num(number):
    if len(number)<2:
        return None
    uniquenum=sorted(list(set(number)))
    if len(uniquenum)<2:
        return None
    else:
        return uniquenum[-2]
my_list=[8,3,6,0,2,4,21,65,98,43,99,54,32]
second_large=second_num(my_list)
print(second_large)
    
