from heapq import *

def find_Kth_smallest2(lists, k):
    '''
    Given ‘M’ sorted arrays,
    find the K’th smallest number among all the arrays.
    '''
    result = -1
    max_heap = []
    pointer = 0
    while lists:
        if len(max_heap) < k:
            heappush(max_heap, -lists[pointer][0])
            del lists[pointer][0]
            if not lists[pointer]:
                del lists[pointer]
        else:
            if -lists[pointer][0] > max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -lists[pointer][0])
            del lists[pointer][0]
            if not lists[pointer]:
                del lists[pointer]

        if lists:
            pointer = (pointer + 1) % len(lists)

    return -max_heap[0]

def find_Kth_smallest(lists, k):
    min_heap = []

    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))

    number_count, number = 0, 0
    while min_heap:
        number, i, list = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break

        if len(list) > i+1:
            heappush(min_heap, (list[i+1], i+1, list))

    return number

def main():
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 2)))

main()
