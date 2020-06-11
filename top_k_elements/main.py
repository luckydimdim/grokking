from heapq import *

def find_k_largest_numbers2(nums, k):
    '''
    Given an unsorted array of numbers,
    find the ‘K’ largest numbers in it.
    '''
    result = []
    min_heap = []

    for num in nums:
        heappush(min_heap, -num)

    for i in range(k):
        result.append(-heappop(min_heap))

    return result

def find_k_largest_numbers(nums, k):
    '''
    Given an unsorted array of numbers,
    find the ‘K’ largest numbers in it.
    '''
    min_heap = []

    for i in range(len(nums)):
        heappush(min_heap, nums[i])
        if i > k - 1:
            heappop(min_heap)

    return list(min_heap)

def main():
    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))

main()

