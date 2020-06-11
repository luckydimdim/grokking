from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
    '''
    Given ‘N’ ropes with different lengths,
    we need to connect these ropes into one big rope with minimum cost.
    The cost of connecting two ropes is equal to the sum of their lengths.
    '''
    result = 0
    min_heap = []
    for rope in ropeLengths:
        heappush(min_heap, rope)

    temp = 0
    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        result += temp
        heappush(min_heap, temp)

    return result

def main():
    print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))

main()

