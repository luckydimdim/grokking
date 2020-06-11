from heapq import *
from collections import deque

def reorganize_string(str, k):
    '''
    Given a string 'str' and a number ‘K’,
    find if the string can be rearranged such
    that the same characters are at least ‘K’
    distance apart from each other.
    '''
    hash_map = {}
    for letter in str:
        hash_map[letter] = hash_map.get(letter, 0) + 1

    max_heap = []
    for letter, rate in hash_map.items():
        heappush(max_heap, (-rate, letter))

    result = ''
    queue = deque()

    while max_heap:
        rate, letter = heappop(max_heap)
        result += letter
        queue.append((rate + 1, letter))

        if len(queue) == k:
            rate, letter = queue.popleft()
            if -rate > 0:
                heappush(max_heap, (rate, letter))

    return result if len(result) == len(str) else ''

def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))

main()
