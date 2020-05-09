def find_averages_of_subarrays(K, arr):
    '''
    Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
    '''
    result = []
    windowSum, windowStart = 0.0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= K - 1:
            result += [windowSum / K]
            windowSum -= arr[windowStart]
            windowStart += 1

    return result

result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print("Averages of subarrays of size K: " + str(result))