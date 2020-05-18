import sys
import math

def smallest_subarray_with_given_sum2(s, arr):
    '''
    Given an array of positive numbers and a positive number ‘S’,
    find the length of the smallest contiguous subarray whose sum
    is greater than or equal to ‘S’. Return 0, if no such subarray exists.
    '''

    window, min_window = 0, sys.maxsize
    window_start, window_sum = 0, 0.0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        window += 1
        while window_sum >= s:
            window_sum -= arr[window_start]
            window_start += 1
            window -= 1
            min_window = min(min_window, window)

    if window_start == 0:
        return 0

    return min_window+1

def smallest_subarray_with_given_sum(s, arr):
    '''
    Given an array of positive numbers and a positive number ‘S’,
    find the length of the smallest contiguous subarray whose sum
    is greater than or equal to ‘S’. Return 0, if no such subarray exists.
    '''

    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_length

print(smallest_subarray_with_given_sum(7, [1, 2, 3, 4]))