def second_num(number):
    if len(number)<2:
        return None
    uniquenum=sorted(list(set(number)))
    if len(uniquenum)<2:
        return None
    else:
        return uniquenum[-2]

