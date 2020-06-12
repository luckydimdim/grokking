from heapq import *

def find_Kth_smallest(matrix, k):
    '''
    Given an N*N matrix where
    each row and column is sorted in ascending order,
    find the Kth smallest element in the matrix.
    '''
    result = -1
    size = len(matrix)

    pointer, col = 0, 0
    while pointer < k:
        row = 0
        while pointer < k and row < size:
            row += 1
            pointer += 1

        col += 1

    return matrix[row-1][col-1]

def find_Kth_smallest(matrix, k):
    min_heap = []

    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    number, counter = 0, 0
    while min_heap:
        number, index, row = heappop(min_heap)
        counter += 1
        if counter == k:
            break

        if len(row) > index+1:
            heappush(min_heap, (row[index+1], index+1, row))

    return number

def main():
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

# [2, 6, 8]
# [3, 7, 10]
# [5, 8, 11]

main()
