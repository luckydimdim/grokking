def search_rotated_array(arr, key):
    '''
    Given an array of numbers which is sorted in ascending order
    and also rotated by some arbitrary number, find if a given ‘key’ is present in it.
    Write a function to return the index of the ‘key’ in the rotated array.
    If the ‘key’ is not present, return -1.
    You can assume that the given array does not have any duplicates.
    '''
    n = len(arr)
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid

        is_asc = arr[start] <= arr[mid]
        if is_asc:
            if arr[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if arr[mid] < key:
                end = mid - 1
            else:
                start = mid + 1

    return -1

def unrotate(arr):
    pass



def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
