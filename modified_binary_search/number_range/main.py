import math

def find_range2(arr, key):
    '''
    Given an array of numbers sorted in ascending order,
    find the range of a given number ‘key’.
    The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
    Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].
    '''
    result = [-1, -1]
    min_index, max_index = math.inf, -math.inf
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            min_index = min(min_index, mid)
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            max_index = max(max_index, mid)
            start = mid + 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    if min_index == math.inf and max_index == -math.inf:
        return [-1, -1]

    return [min_index, max_index]

def find_range(arr, key):
    '''
    Given an array of numbers sorted in ascending order,
    find the range of a given number ‘key’.
    The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
    Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].
    '''
    result = [-1, -1]
    result[0] = binary_search(arr, key, 'min')
    if result[0] != -1:
        result[1] = binary_search(arr, key, 'max')
    return result

def binary_search(arr, key, scale):
    index = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            index = mid
            if scale == 'min':
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return index

def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
