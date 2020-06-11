from heapq import *

def find_k_frequent_numbers2(nums, k):
    '''
    Given an unsorted array of numbers,
    find the top ‘K’ frequently occurring numbers in it.
    '''
    max_heap = []
    hash_map = {}

    for num in nums:
        if num not in hash_map:
            hash_map[num] = 0
        hash_map[num] += 1

    for num in hash_map:
        heappush(max_heap, (-hash_map[num], num))

    result = []
    for i in range(k):
        result.append(heappop(max_heap)[1])

    return result

def find_k_frequent_numbers(nums, k):
    min_heap = []
    hash_map = {}

    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    for num, rate in hash_map.items():
        heappush(min_heap, (rate, num))
        if len(min_heap) > k:
            heappop(min_heap)

    return [x[1] for x in list(min_heap)]

def main():
    print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))

main()

