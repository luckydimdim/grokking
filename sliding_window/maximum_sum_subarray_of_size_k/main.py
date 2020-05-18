def max_sub_array_of_size_k(k, arr):
    '''
    Given an array of positive numbers and a positive number ‘k’,
    find the maximum sum of any contiguous subarray of size ‘k’.
    '''

    window_sum, max_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum

def max_sub_array_of_size_k_brute(k, arr):
    max_sum, current_sum = 0, 0

    for i in range(len(arr) - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += arr[j]
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_sub_array_of_size_k(2, [1, 2, 3, 4, 5]))