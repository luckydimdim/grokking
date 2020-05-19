import math

def triplet_sum_close_to_target(arr, target_sum):
    '''
    Given an array of unsorted numbers and a target number, find a triplet
    in the array whose sum is as close to the target number as possible,
    return the sum of the triplet. If there are more than one such triplet,
    return the sum of the triplet with the smallest sum.
    '''

    arr.sort()
    smallest_diff = math.inf

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]

            if target_diff == 0:
                return target_sum

            if abs(target_diff) < abs(smallest_diff) or (abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff):
                smallest_diff = target_diff

            if target_diff > 0:
                left += 1
            else:
                right -= 1

    return target_sum - smallest_diff

#         |
array = [-3, -1, 1, 2]
#            l     r
# 2
target = 1

print(triplet_sum_close_to_target(array, target))