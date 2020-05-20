from collections import deque

def find_subarrays(arr, target):
    '''
    Given an array with positive numbers and a target number,
    find all of its contiguous subarrays whose product is less than the target number.
    '''
    result = []
    product = 1
    left = 0

    for right in range(len(arr)):
        product *= arr[right]

        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1

        temp = []
        for i in range(right, left - 1, -1):
            temp.append(arr[i])
            result.append(list(temp))

    return result

arr = [2, 5, 3, 10]
target = 30

print(find_subarrays(arr, target))