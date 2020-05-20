def dutch_flag_sort2(arr):
    '''
    Given an array containing 0s, 1s and 2s, sort the array in-place.
    You should treat numbers of the array as objects, hence, we can’t
    count 0s, 1s, and 2s to recreate the array.
    The flag of the Netherlands consists of three colors:
    red, white and blue; and since our input array also consists of three different numbers
    that is why it is called Dutch National Flag problem.
    '''

    left, right = 0, 0
    current = 0

    while right < len(arr):
        if arr[right] == current:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
        right += 1

    current = 1
    right = left

    while right < len(arr):
        if arr[right] == current:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
        right += 1

    return arr


def dutch_flag_sort(arr):
    '''
    Given an array containing 0s, 1s and 2s, sort the array in-place.
    You should treat numbers of the array as objects, hence, we can’t
    count 0s, 1s, and 2s to recreate the array.
    The flag of the Netherlands consists of three colors:
    red, white and blue; and since our input array also consists of three different numbers
    that is why it is called Dutch National Flag problem.
    '''
    low, high = 0, len(arr) - 1
    pointer = 0

    while pointer <= high:
        if arr[pointer] == 0:
            arr[low], arr[pointer] = arr[pointer], arr[low]
            low += 1
            pointer += 1
        elif arr[pointer] == 2:
            arr[high], arr[pointer] = arr[pointer], arr[high]
            high -= 1
        elif arr[pointer] == 1:
            pointer += 1

    return arr

arr = [1, 0, 2, 1, 0]
print(dutch_flag_sort(arr))