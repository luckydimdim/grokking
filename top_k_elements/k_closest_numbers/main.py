from heapq import *

def find_closest_elements(arr, K, X):
    '''
    Given a sorted number array and two integers ‘K’ and ‘X’,
    find ‘K’ closest numbers to ‘X’ in the array.
    Return the numbers in the sorted order.
    ‘X’ is not necessarily present in the array.
    '''
    result = []

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == X:
            break

        if arr[mid] < X:
            start = mid + 1
        else:
            end = mid - 1

        if start > 0:
            mid = start - 1

    low, high = max(mid - K, 0), min(mid + K, len(arr) - 1)

    min_heap = []

    for i in range(low, high + 1):
        diff = abs(arr[i] - X)
        heappush(min_heap, (diff, arr[i]))

    result = []
    for i in range(K):
        result.append(heappop(min_heap)[1])

    result.sort()

    return result


def main():
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))

main()
