def search_triplets(arr):
    '''
    Given an array of unsorted numbers,
    find all unique triplets in it that add up to zero.
    '''
    triplets = []
    pointer = 0

    arr.sort()

    while pointer < len(arr) - 2:
        if pointer > 0 and arr[pointer] == arr[pointer - 1]:
            continue

        left, right = pointer + 1, len(arr) - 1

        while left <= right:
            current_sum = arr[pointer] + arr[left] + arr[right]

            if current_sum == 0 and arr[left] == arr[left - 1]:
                left += 1
            elif current_sum == 0 and right < len(arr) - 1 and arr[right] == arr[right + 1]:
                right -= 1
            elif current_sum == 0:
                triplets.append([arr[pointer], arr[left], arr[right]])
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                left += 1

        pointer += 1

    return triplets

array = [-3, 0, 1, 2, -1, 1, -2]
print(search_triplets(array))