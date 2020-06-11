from heapq import *

def sort_character_by_frequency(str):
    '''
    Given a string, sort it based on the decreasing frequency of its characters.
    '''
    hash_map = {}
    for letter in str:
        hash_map[letter] = hash_map.get(letter, 0) + 1

    max_heap = []
    for letter, rate in hash_map.items():
        heappush(max_heap, (-rate, letter))

    result = ''
    while max_heap:
        rate, letter = heappop(max_heap)

        for i in range(-rate):
            result += letter

    return result

def main():
    print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))

main()
