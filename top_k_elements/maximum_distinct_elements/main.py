from heapq import *

def find_maximum_distinct_elements(nums, k):
    '''
    Given an array of numbers and a number ‘K’,
    we need to remove ‘K’ numbers from the array
    such that we are left with maximum distinct numbers.
    '''
    result = 0
    if len(nums) <= k:
        return result

    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    min_heap = []
    for num, rate in hash_map.items():
        if rate > 1:
            heappush(min_heap, (rate, num))
        else:
            result += 1

    times = 0
    while times < k and min_heap:
        rate, num = heappop(min_heap)
        rate -= 1

        if rate == 1:
            result += 1
        else:
            heappush(min_heap, (rate - 1, num))
        times += 1

    for _ in range(times, k):
        result -= 1

    return result


def main():
    print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))

main()

