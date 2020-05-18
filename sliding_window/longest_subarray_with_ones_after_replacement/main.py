def length_of_longest_substring2(arr, k):
    '''
    Given an array containing 0s and 1s,
    if you are allowed to replace no more than ‘k’ 0s with 1s,
    find the length of the longest contiguous subarray having all 1s.
    '''
    window_start, max_length = 0, 0
    counter = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 0:
            arr[window_end] = -1
            counter += 1

        while counter > k:
            if arr[window_start] == -1:
                arr[window_start] = 0
                counter -= 1
                window_start += 1
            else:
                window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

def length_of_longest_substring(arr, k):
    '''
    Given an array containing 0s and 1s,
    if you are allowed to replace no more than ‘k’ 0s with 1s,
    find the length of the longest contiguous subarray having all 1s.
    '''
    window_start, max_length = 0, 0
    max_ones_counter = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_counter += 1

        if window_end - window_start + 1 - max_ones_counter > k:
            if arr[window_start] == 1:
                max_ones_counter -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k = 2

print(length_of_longest_substring(array, k))