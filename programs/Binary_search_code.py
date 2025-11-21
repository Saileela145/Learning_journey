def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    arr = [2, 3, 5, 7, 43, 45, 87]   # sorted list
    x = 43

    result = binary_search(arr, x)

    if result != -1:
        print("Element present at index", result)
    else:
        print("Element not present")
