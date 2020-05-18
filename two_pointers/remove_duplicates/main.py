def remove_duplicates2(arr):
    '''
    Given an array of sorted numbers, remove all duplicates from it.
    You should not use any extra space; after removing the duplicates
    in-place return the new length of the array.
    '''

    pointer = 0

    while pointer < len(arr) - 1:
        if arr[pointer] == arr[pointer + 1]:
            del arr[pointer + 1]
        else:
            pointer += 1

    return len(arr)

def remove_duplicates(arr):
    '''
    Given an array of sorted numbers, remove all duplicates from it.
    You should not use any extra space; after removing the duplicates
    in-place return the new length of the array.
    '''

    left = 0

    for right in range(1, len(arr)):
        if arr[right] != arr[left]:
            left += 1
            arr[right], arr[left] = arr[left], arr[right]

    return left + 1

arr = [2, 3, 3, 3, 6, 9, 9]
print(remove_duplicates(arr))