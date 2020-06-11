from heapq import *

def rearrange_string2(str):
    '''
    Given a string, find if its letters can be rearranged
    in such a way that no two same characters come next to each other.
    '''
    hash_map = {}
    for letter in str:
        hash_map[letter] = hash_map.get(letter, 0) + 1

    max_heap = []
    for letter, rate in hash_map.items():
        heappush(max_heap, (-rate, letter))

    last_letter, result = '', ''
    while max_heap:
        rate1, letter1 = heappop(max_heap)

        if letter1 == last_letter:
            return ''

        rate1 += 1
        if -rate1 > 0:
            heappush(max_heap, (rate1, letter1))

        result += letter1

        if max_heap:
            rate2, letter2 = heappop(max_heap)
            rate2 += 1
            if -rate2 > 0:
                heappush(max_heap, (rate2, letter2))

            last_letter = letter2
            result += letter2

    return result

def rearrange_string(str):
    '''
    Given a string, find if its letters can be rearranged
    in such a way that no two same characters come next to each other.
    '''
    hash_map = {}
    for letter in str:
        hash_map[letter] = hash_map.get(letter, 0) + 1

    max_heap = []
    for letter, rate in hash_map.items():
        heappush(max_heap, (-rate, letter))

    last_letter, last_rate, result = None, 0, ''
    while max_heap:
        rate, letter = heappop(max_heap)

        if last_letter and -last_rate > 0:
            heappush(max_heap, (last_rate, last_letter))

        result += letter

        last_letter = letter
        last_rate = rate + 1

    return result if len(result) == len(str) else ''

def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))

main()

