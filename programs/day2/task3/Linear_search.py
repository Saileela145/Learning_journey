def linear_search(num, target):
    for i, value in enumerate(num):
        if value == target:
            return i
    return -1
