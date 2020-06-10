def find_max_in_bitonic_array(arr):
    '''
    Find the maximum value in a given Bitonic array.
    An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
    Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
    '''
    n = len(arr)
    start, end = 0, n - 1
    while start < end:
        mid = start + (end - start) // 2
        is_asc = arr[mid] < arr[mid + 1]

        if is_asc:
            start = mid + 1
        else:
            end = mid - 1

    return arr[start]

def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))

main()
