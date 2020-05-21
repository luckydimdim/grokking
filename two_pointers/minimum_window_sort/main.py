import math

def shortest_window_sort2(arr):
    '''
    Given an array, find the length of the smallest subarray
    in it which when sorted will sort the whole array.
    '''

    unsorted = list(arr)
    arr.sort()

    left, right = 0, len(arr) - 1
    top, bottom = -1, -1

    while left <= right:
        if arr[left] != unsorted[left] and bottom == -1:
            bottom = left

        if arr[right] != unsorted[right] and top == -1:
            top = right

        left += 1
        right -= 1

    if top == bottom:
        return 0

    return top - bottom + 1

def shortest_window_sort(arr):
    '''
    Given an array, find the length of the smallest subarray
    in it which when sorted will sort the whole array.
    '''

    left, right = 0, len(arr) - 1
    bottom, top = -1, -1

    while left < len(arr) - 1 and arr[left] < arr[left + 1]:
        left += 1

    if left == len(arr) - 1:
        return 0

    bottom = left

    while right > 0 and arr[right] > arr[right - 1]:
        right -= 1

    top = right

    minimum, maximum = math.inf, -math.inf

    for i in range(bottom, top + 1):
        minimum = min(minimum, arr[i])
        maximum = max(maximum, arr[i])

    left, right = bottom, top

    while bottom >= 0:
        if arr[bottom] > minimum:
            left = bottom
        bottom -= 1

    while top < len(arr):
        if arr[top] < maximum:
            right = top
        top += 1

    return right - left + 1

#         |
arr = [1, 3, 2, 0, -1, 7, 10]
#                   |

print(shortest_window_sort(arr))