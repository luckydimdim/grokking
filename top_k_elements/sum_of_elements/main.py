from heapq import *

def find_sum_of_elements(nums, k1, k2):
    '''
    Given an array, find the sum of all numbers
    between the K1’th and K2’th smallest elements of that array.
    '''
    result = 0
    min_heap = []

    for num in nums:
        heappush(min_heap, num)

    for _ in range(k1):
        heappop(min_heap)

    for _ in range(k2 - k1 - 1):
        result += heappop(min_heap)

    return result

def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))

main()
