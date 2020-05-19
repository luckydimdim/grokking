def triplet_with_smaller_sum2(arr, target):
    '''
    Given an array arr of unsorted numbers and a target sum,
    count all triplets in it such that arr[i] + arr[j] + arr[k] < target
    where i, j, and k are three different indices.
    Write a function to return the count of such triplets.
    '''
    count, pointer = 0, 0

    arr.sort()
    print(arr)

    while pointer < len(arr) - 2:
        left = pointer + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[pointer] + arr[left] + arr[right]

            if current_sum >= target:
                right -= 1
                continue

            i = right
            while i > left:
                if arr[pointer] != arr[left] and arr[pointer] != arr[i] and arr[left] != arr[i]:
                    count += 1
                i -= 1

            left += 1

        pointer += 1

    return count

def triplet_with_smaller_sum(arr, target):
    '''
    Given an array arr of unsorted numbers and a target sum,
    count all triplets in it such that arr[i] + arr[j] + arr[k] < target
    where i, j, and k are three different indices.
    Write a function to return the count of such triplets.
    '''
    triplets = []
    pointer = 0

    arr.sort()

    while pointer < len(arr) - 2:
        left = pointer + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[pointer] + arr[left] + arr[right]

            if current_sum >= target:
                right -= 1
                continue

            for i in range(right, left, -1):
                if arr[pointer] != arr[left] and arr[pointer] != arr[i] and arr[left] != arr[i]:
                    triplets.append([arr[pointer], arr[left], arr[i]])

            left += 1

        pointer += 1

    return triplets

arr = [-1, 4, 2, 1, 3]
target = 5

print(triplet_with_smaller_sum2(arr, target))