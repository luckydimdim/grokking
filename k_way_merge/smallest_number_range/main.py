from heapq import *
import math

def find_smallest_range(lists):
    '''
    Given ‘M’ sorted arrays, find the smallest range that
    includes at least one number from each of the ‘M’ lists.
    '''
    min_heap = []
    curr_max, diff, curr_min = -math.inf, math.inf, math.inf
    for row in lists:
        heappush(min_heap, (row[0], 0, row))
        curr_max = max(curr_max, row[0])

    while len(min_heap) == len(lists):
        number, index, row = heappop(min_heap)

        if curr_max - number < diff:
            curr_min = number
            diff = curr_max - number

        if len(row) > index + 1:
            curr_max = max(curr_max, row[index+1])
            heappush(min_heap, (row[index+1], index+1, row))

    return [curr_min, curr_max]


def main():
    print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))

    print("Smallest range is: " +
        str(find_smallest_range([[1, 9], [4, 12], [7, 10, 16]])))

main()

